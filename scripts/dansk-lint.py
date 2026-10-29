#!/usr/bin/env python3
"""Deterministisk tjek af dansk tekst for AI-sprog og tung sætningsbygning.

Tjekket ser kun på mønstre, som et program kan finde sikkert uden en ordbog
eller en grammatisk analyse. Det markerer aldrig forbehold som "måske",
"muligvis" eller "kan have fejlet". Forbehold er indhold, ikke stil.

Brug:
    dansk-lint.py FIL [FIL ...]
    echo "tekst" | dansk-lint.py [--json]
    dansk-lint.py --baseline 5 FIL         # bestået, hvis der højst er 5 fejl
    dansk-lint.py --disable passiv,papirord FIL
    dansk-lint.py --selftest

Exitkode 1: der er flere fejl ("fejl") end baseline (standard 0).
Fund på niveauet "råd" får aldrig tjekket til at fejle.
Exitkode 2: forkert brug (ukendt flag, forkert værdi, ukendt regel, fil kan ikke læses).
"""
import argparse
import json
import re
import sys

FEJL = "fejl"
RAAD = "råd"

MAX_WORDS = 25  # loft for beskrivelser. Loftet for instruktioner er 20, men tjekket kan ikke se forskel.
LONG_COMPOUND = 22  # bogstaver


def _rx(*phrases):
    return re.compile(r"\b(?:" + "|".join(phrases) + r")\b", re.I)


# (id, niveau, mønster, besked)
RULES = [
    ("semikolon", FEJL, re.compile(r";"),
     "Brug ikke semikolon. Del sætningen i to sætninger."),
    ("ai-floskel", FEJL, _rx(
        r"det er (?:vigtigt|værd|afgørende|centralt) at (?:bemærke|understrege|huske|nævne|notere|fremhæve)",
        r"i nutidens \w+", r"i dagens (?:hurtige|digitale|moderne|travle) \w+",
        r"i en verden,? hvor", r"lad os (?:dykke|kigge nærmere|udforske)",
        r"dykke(?:r|de|t)? (?:dybere |ned )?(?:i|ned i)", r"spiller en (?:afgørende|central|vigtig|nøgle)\s?rolle",
        r"et væld af", r"en bred vifte af", r"et rigt (?:tapet|tæppe)", r"uanset om du er",
        r"godt spørgsmål", r"jeg håber,? (?:dette|det) hjælper", r"sig (?:endelig )?til,? hvis",
        r"(?:frigør|frigøre|låse? op for|udnytte) (?:\w+ )?(?:fulde |hele )?potentiale(?:t)?",
        r"til (?:det )?næste niveau", r"det (?:digitale|teknologiske|moderne) landskab",
        r"navigere(?:r)? (?:i|gennem) (?:kompleksiteten|landskabet|udfordringerne)",
    ), "Tom AI-floskel. Slet den, eller skriv den konkrete oplysning."),
    ("hype-ord", FEJL, _rx(
        r"banebrydende", r"sømløs(?:t|e)?", r"robust(?:e)?", r"kraftfuld(?:t|e)?", r"problemfri(?:t|e)?",
        r"gnidningsfri(?:t|e)?", r"revolutionerende", r"state[- ]of[- ]the[- ]art", r"cutting[- ]edge",
        r"game[- ]?changer", r"i verdensklasse", r"lynhurtig(?:t|e)?", r"ubesværet", r"skræddersye(?:t|de)",
        r"enestående", r"uovertruffen(?:t)?", r"uovertrufne",
    ), "Hype-ord. Slet det, eller skriv det tal eller den målbare egenskab, som ordet påstår."),
    ("kalke", FEJL, _rx(
        r"række(?:r|de)? ud til", r"rakte ud til", r"adressere(?:r|de|t)?",
        r"på (?:en )?(?:daglig|ugentlig|månedlig|årlig|regelmæssig|løbende) basis",
        r"levere(?:r|de|t)? på", r"tage(?:r)? ejerskab", r"tog ejerskab", r"eksekvere(?:r|de|t)?",
        r"i sidste ende", r"ved dagens afslutning", r"i slutningen af dagen", r"gøre en forskel",
    ), "Vending oversat ord for ord fra engelsk. Brug det almindelige danske ord (fx kontakte, løse, dagligt, udføre)."),
    ("substantivsyge", FEJL, re.compile(
        r"\b(?:foretage|foretager|foretog|foretaget|gennemføre|gennemfører|gennemførte|gennemført"
        r"|udføre|udfører|udførte|udført|tage|tager|tog|truffet|træffe|træffer|traf)\s+"
        r"(?:en|et|den|det|de)?\s*(?:\w+\s+)?(?:\w+(?:ing|ingen|else|elsen|tion|tionen|sion|sionen|ering|eringen)|\w*(?:analyse|analysen|gennemgang|gennemgangen|kontrol|kontrollen))\b"
        r"|\b\w+(?:ing|ingen|else|elsen|tion|tionen)\s+(?:finder|fandt|vil finde|skal finde|kan finde)\s+sted\b",
        re.I),
     "Handling gemt i et navneord. Brug verbet (vurdere, ikke foretage en vurdering)."),
    ("konstrueret-kontrast", RAAD, re.compile(
        r"\bikke (?:bare|kun|blot)\b[^.!?\n]{1,80}?(?:[–—]|\bdet er\b|\bmen også\b)", re.I),
     "Mulig konstrueret kontrast (\"ikke bare X – det er Y\"). Skriv påstanden direkte."),
    ("passiv", RAAD, re.compile(
        r"\b(?:bliver|blev|blevet|blive)\s+(?:\w+\s+)?\w+(?:et|ede|te)\b"
        r"|\b(?:kan|skal|må|bør|vil|kunne|skulle|måtte|burde|ville)\s+(?:ikke\s+|også\s+|nu\s+)?"
        r"(?!(?:findes|synes|lykkes|mindes|trives|færdes|ses|slås|enes|ske)\b)\w{2,}es\b",
        re.I),
     "Mulig passiv. Nævn den, der handler, og brug aktiv form. Behold passiv, hvis den handlende er ukendt eller uvæsentlig."),
    ("papirord", RAAD, _rx(
        r"såfremt", r"endvidere", r"ydermere", r"hvorledes", r"hvorvidt", r"vedrørende",
        r"i henhold til", r"i medfør af", r"med henblik på", r"under henvisning til", r"forefindes",
        r"erholde(?:r)?", r"fremsende(?:r|nde)?", r"fremsendt", r"foranledige(?:r)?", r"påbegynde(?:r)?",
        r"iværksætte(?:r)?", r"tilstræbe(?:r)?", r"nærværende", r"ovennævnte", r"ovenstående",
        r"nedenstående", r"efterfølgende", r"pågældende",
    ), "Papirord. Brug et hverdagsord (hvis, også, om, sende, begynde, senere)."),
    ("sætningsforlænger", RAAD, re.compile(
        r",\s*(?:idet|hvilket|hvorfor|hvoraf|hvorved|hvormed|ligesom)\b", re.I),
     "Sætningsforlænger. Sæt punktum, og begynd en ny sætning."),
]

# Ét ord, én betydning: grupper af verber, som ofte skifter for den samme handling.
SYNONYM_GROUPS = [
    {"tjekke": r"tjek(?:ke|ker|kede|ket)?", "kontrollere": r"kontroll(?:ere|erer|erede|eret|ér)",
     "verificere": r"verific(?:ere|erer|erede|eret|ér)", "validere": r"valid(?:ere|erer|erede|eret|ér)",
     "bekræfte": r"bekræft(?:e|er|ede|et)?"},
    {"slette": r"slet(?:te|ter|tede|tet)|slet(?!\s+ikke)", "fjerne": r"fjern(?:e|er|ede|et)?"},
    {"starte": r"start(?:e|er|ede|et)?", "begynde": r"begynd(?:e|er|te)?|begyndt",
     "påbegynde": r"påbegynd(?:e|er|te)|påbegyndt", "igangsætte": r"igangsæt(?:te|ter)|igangsat",
     "initiere": r"initi(?:ere|erer|erede|eret)"},
    {"stoppe": r"stop(?:pe|per|pede|pet)?", "standse": r"stands(?:e|er|ede|et)?",
     "terminere": r"termin(?:ere|erer|erede|eret)"},
    {"vise": r"vise|viser|viste", "fremvise": r"fremvis(?:e|er|te|t)"},
    {"bruge": r"bruge|bruger|brugte", "anvende": r"anvend(?:e|er|te|t)?", "benytte": r"benytt?(?:e|er|ede|et)",
     "udnytte": r"udnytt?(?:e|er|ede|et)"},
    {"reparere": r"repar(?:ere|erer|erede|eret)", "fikse": r"fiks(?:e|er|ede|et)"},
    {"sende": r"send(?:e|er|te|t)?", "fremsende": r"fremsend(?:e|er|te|t)?"},
    {"hente": r"hent(?:e|er|ede|et)?", "indhente": r"indhent(?:e|er|ede|et)?", "fremskaffe": r"fremskaff(?:e|er|ede|et)"},
    {"ændre": r"ændr(?:e|er|ede|et)?", "modificere": r"modific(?:ere|erer|erede|eret)"},
]
SYNONYM_RES = [{base: re.compile(r"\b(?:" + rx + r")\b", re.I) for base, rx in group.items()}
               for group in SYNONYM_GROUPS]

CODE_FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`]*`")
URL = re.compile(r"<?\b(?:https?|ftp)://\S+|\S+@\S+\.\w+")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
TABLE_ROW = re.compile(r"^\s*\|")
TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{3,}")
QUOTE = re.compile(r"^\s{0,3}(?:>\s?)+")
WORD_CHAR = re.compile(r"[^\W_]")
LETTERS = re.compile(r"^[^\W\d_]+$")
SENTENCE_END = re.compile(r"[.!?][\"'”’)\]*_]*$")
# Forkortelser, hvis punktum aldrig slutter en sætning.
ABBREVIATIONS = {"f.eks.", "bl.a.", "dvs.", "osv.", "mv.", "m.v.", "ca.", "jf.", "nr.", "kl.", "pkt.",
                 "stk.", "evt.", "inkl.", "ekskl.", "mht.", "vedr.", "iht.", "pga.", "ifm.", "o.l.",
                 "m.fl.", "s.", "hhv.", "fig.", "tlf.", "vs.", "e.g.", "i.e.", "etc."}


def _mask(text):
    """Erstat kode og URL'er med mellemrum, så kolonnerne passer."""
    text = INLINE_CODE.sub(lambda m: " " * len(m.group(0)), text)
    return URL.sub(lambda m: " " * len(m.group(0)), text)


def _blocks(lines):
    """Saml linjer til blokke af prosa: (start_linje, [(linjenr, tekst)])."""
    blocks, current, in_fence = [], [], False

    def flush():
        if current:
            blocks.append(list(current))
            current.clear()

    for n, raw in enumerate(lines, 1):
        if CODE_FENCE.match(raw):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = QUOTE.sub("", raw)
        if TABLE_SEP.match(line):
            continue
        if TABLE_ROW.match(line):
            flush()
            for cell in line.strip().strip("|").split("|"):
                if cell.strip():
                    blocks.append([(n, cell)])
            continue
        if not line.strip() or HEADING.match(line):
            flush()
            continue
        marker = LIST_ITEM.match(line)
        if marker:
            flush()
            line = " " * marker.end() + line[marker.end():]
        current.append((n, line))
    flush()
    return blocks


def _sentences(block):
    """Del en blok i sætninger. Giver (linjenr, kolonne, antal ord, tekst)."""
    tokens = []
    for n, line in block:
        for m in re.finditer(r"\S+", _mask(line)):
            tokens.append((n, m.start() + 1, m.group(0)))
    sentence = []
    for i, tok in enumerate(tokens):
        sentence.append(tok)
        word = tok[2]
        nxt = tokens[i + 1][2] if i + 1 < len(tokens) else None
        if not SENTENCE_END.search(word):
            continue
        bare = word.lower().rstrip("\"'”’)]*_")
        if bare in ABBREVIATIONS:
            continue
        if nxt is not None and not (nxt.lstrip("\"'“‘([*_")[:1].isupper() or nxt[:1].isdigit()):
            continue
        yield sentence
        sentence = []
    if sentence:
        yield sentence


def lint(text, filename="<stdin>"):
    findings = []
    words_total = 0
    lines = text.splitlines()
    seen = {}
    for block in _blocks(lines):
        for n, line in block:
            masked = _mask(line)
            words_total += sum(1 for t in masked.split() if WORD_CHAR.search(t))
            for rule_id, level, pattern, msg in RULES:
                for m in pattern.finditer(masked):
                    findings.append({"file": filename, "line": n, "col": m.start() + 1,
                                     "rule": rule_id, "level": level,
                                     "match": m.group(0), "message": msg})
            for m in re.finditer(r"[^\W\d_][\w-]*", masked):
                word = m.group(0)
                if len(word) >= LONG_COMPOUND and LETTERS.match(word) and word.islower():
                    findings.append({"file": filename, "line": n, "col": m.start() + 1,
                                     "rule": "lang-sammensætning", "level": RAAD, "match": word,
                                     "message": "Langt sammensat ord. Del det op (mulighed for dispensation, ikke dispensationsmulighed)."})
            for gi, group in enumerate(SYNONYM_RES):
                for base, pattern in group.items():
                    if (gi, base) not in seen:
                        m = pattern.search(masked)
                        if m:
                            seen[(gi, base)] = (n, m.start() + 1, m.group(0))
        for sentence in _sentences(block):
            count = sum(1 for _, _, w in sentence if WORD_CHAR.search(w))
            if count > MAX_WORDS:
                n, col, _ = sentence[0]
                preview = " ".join(w for _, _, w in sentence[:8]) + " ..."
                findings.append({"file": filename, "line": n, "col": col, "rule": "lang-sætning",
                                 "level": FEJL, "match": preview,
                                 "message": f"Sætningen har {count} ord (højst {MAX_WORDS}). Del den op."})
    for gi, group in enumerate(SYNONYM_RES):
        present = sorted((seen[(gi, b)], b) for b in group if (gi, b) in seen)
        for (n, col, match), base in present[1:]:
            findings.append({"file": filename, "line": n, "col": col, "rule": "synonymrotation",
                             "level": FEJL, "match": match,
                             "message": f"'{base}' og '{present[0][1]}' betyder den samme handling. Vælg ét ord, og brug det hver gang."})
    findings.sort(key=lambda f: (f["line"], f["col"]))
    return findings, words_total


RULE_IDS = {r[0] for r in RULES} | {"lang-sætning", "lang-sammensætning", "synonymrotation"}


def report(findings, words_total, as_json, hard, baseline):
    rate = round(len(findings) * 100 / words_total, 1) if words_total else 0.0
    if as_json:
        print(json.dumps({"findings": findings, "count": len(findings), "hard_count": hard,
                          "baseline": baseline, "words": words_total, "per_100_words": rate},
                         indent=2, ensure_ascii=False))
        return
    for f in findings:
        print(f"{f['file']}:{f['line']}:{f['col']} {f['rule']} ({f['level']}): {f['message']} [{f['match']}]")
    print(f"\n{len(findings)} fund ({hard} fejl, baseline {baseline}), {words_total} ord, {rate} pr. 100 ord")
    print("Forbehold (måske, muligvis, kan have) bliver aldrig markeret. Forbehold er indhold.")


def selftest():
    def rules(text):
        return {f["rule"] for f in lint(text)[0]}

    bad = ("Det er vigtigt at bemærke, at vi tilbyder en sømløs løsning; den er robust. "
           "Vi rækker ud til kunden på daglig basis. Vi foretager en vurdering af sagen. "
           "Filen bliver slettet af systemet. Formularen skal udfyldes. "
           "Såfremt du har spørgsmål, kan du skrive til os, hvilket vi sætter pris på.")
    got = rules(bad)
    for expected in ("ai-floskel", "semikolon", "hype-ord", "kalke", "substantivsyge",
                     "passiv", "papirord", "sætningsforlænger"):
        assert expected in got, (expected, got)
    # forbehold er indhold
    assert not lint("Anmodningen kan have fejlet. Måske er serveren nede. Det skyldes muligvis netværket.")[0]
    # deponensverber er ikke passiv
    assert "passiv" not in rules("Filen skal findes i mappen. Det kan ses i loggen.")
    # "slet ikke" er ikke verbet slette
    assert "synonymrotation" not in rules("Fjern filen. Den er slet ikke nødvendig.")
    assert "synonymrotation" in rules("Slet filen. Fjern derefter mappen.")
    assert "synonymrotation" in rules("Tjek loggen. Verificér derefter resultatet.")
    # lange sætninger, forkortelser og ordenstal
    long = " ".join(["ord"] * 26) + "."
    assert "lang-sætning" in rules(long)
    assert "lang-sætning" not in rules(" ".join(["ord"] * 25) + ".")
    short = "Brug fx Python 3.12, bl.a. til test. Den 3. maj skal du opdatere. Kør f.eks. testen igen."
    assert "lang-sætning" not in rules(short)
    # kode, URL'er og kodeblokke tæller ikke
    assert not lint("Kør `foo; bar` nu. Se https://example.com/a;b for mere.")[0]
    assert not lint("```\nDet er vigtigt at bemærke; robust.\n```\n")[0]
    # tabelceller og listepunkter er hver deres blok
    table = "| A | B |\n|---|---|\n| " + " ".join(["ord"] * 20) + " | " + " ".join(["ord"] * 20) + " |\n"
    assert "lang-sætning" not in rules(table)
    items = "- " + " ".join(["ord"] * 20) + "\n- " + " ".join(["ord"] * 20) + "\n"
    assert "lang-sætning" not in rules(items)
    # lange sammensatte ord
    assert "lang-sammensætning" in rules("Se sagsbehandlingsspørgsmålene her.")
    # konstrueret kontrast
    assert "konstrueret-kontrast" in rules("Det er ikke bare et værktøj – det er en partner.")
    # kommandolinjen
    for args in (["--basline", "3"], ["--baseline", "x"], ["--baseline", "-1"], ["--disable", "passive"]):
        try:
            import contextlib, io
            with contextlib.redirect_stderr(io.StringIO()):
                main(args)
        except SystemExit as e:
            assert e.code == 2, (args, e.code)
        else:
            raise AssertionError(args)
    print("selftest OK")


def _rule_list(value):
    rules = {r for r in value.split(",") if r}
    unknown = rules - RULE_IDS
    if unknown:
        raise argparse.ArgumentTypeError(
            f"ukendt regel: {', '.join(sorted(unknown))}. Kendte regler: {', '.join(sorted(RULE_IDS))}")
    return rules


def _non_negative_int(value):
    try:
        n = int(value)
    except ValueError:
        n = -1
    if n < 0:
        raise argparse.ArgumentTypeError(f"forventede et heltal på 0 eller mere, fik {value!r}")
    return n


def main(argv):
    parser = argparse.ArgumentParser(
        prog="dansk-lint.py", allow_abbrev=False,
        description="Tjek dansk tekst for AI-sprog og tung sætningsbygning. Læser stdin, hvis du ikke angiver en FIL.")
    parser.add_argument("paths", nargs="*", metavar="FIL")
    parser.add_argument("--json", action="store_true", help="skriv fundene som JSON")
    parser.add_argument("--baseline", type=_non_negative_int, default=0, metavar="N",
                        help="bestået, hvis der højst er N fejl (standard 0)")
    parser.add_argument("--disable", type=_rule_list, default=set(), metavar="REGLER",
                        help="regel-id'er adskilt af komma, som tjekket ikke skal vise")
    parser.add_argument("--selftest", action="store_true", help="kør de indbyggede test")
    args = parser.parse_intermixed_args(argv)
    if args.selftest:
        selftest()
        return 0
    findings, words = [], 0
    if args.paths:
        for p in args.paths:
            try:
                with open(p, encoding="utf-8") as fh:
                    text = fh.read()
            except OSError as e:
                parser.error(f"kan ikke læse {p}: {e.strerror}")
            f, w = lint(text, p)
            findings.extend(f)
            words += w
    else:
        findings, words = lint(sys.stdin.read())
    findings = [f for f in findings if f["rule"] not in args.disable]
    hard = sum(1 for f in findings if f["level"] == FEJL)
    report(findings, words, args.json, hard, args.baseline)
    return 1 if hard > args.baseline else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
