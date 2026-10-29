# llm-anti-slop-danish

En skill til AI-agenter, som får dem til at skrive klart dansk uden AI-sprog ("slop"). Skillen hedder `anti-slop-dansk`.

Skillen bygger på principperne i ASD-STE100 Simplified Technical English og på Dansk Sprognævns råd om klarsprog. Den passer til tekst, som en anden agent eller et menneske skal forstå på én måde: fejlbeskeder, værktøjsbeskrivelser, instruktioner, systemprompter, dokumentation, commit-beskeder og PR-beskrivelser.

Der findes ingen officiel dansk udgave af STE. Skillen er derfor et værktøj til klar tekst, ikke en certificeret standard.

## Indhold

| Fil | Indhold |
|---|---|
| `SKILL.md` | Instruktionerne til agenten: to niveauer (Streng og Let), regler for sætningsbygning og ordvalg, tjekliste for AI-sprog, fremgangsmåde og outputformat. |
| `references/ordliste.md` | Papirord, substantivsyge, oversatte vendinger, AI-floskler, hype-ord og synonymgrupper, med det ord, som du skal bruge i stedet. |
| `references/kilder.md` | Kilderne og forskellene mellem STE og dansk. |
| `examples/foer-efter.md` | Omskrivninger før og efter. |
| `scripts/dansk-lint.py` | Et deterministisk tjek uden eksterne pakker. |

## Installation

Kopiér mappen til mappen med skills for din agent. For OpenCode:

```sh
git clone https://github.com/glutter/llm-anti-slop-danish ~/.config/opencode/skills/anti-slop-dansk
```

For Claude Code skal du bruge `~/.claude/skills/anti-slop-dansk`.

Agenten bruger skillen, når opgaven passer til beskrivelsen i `SKILL.md`. Du kan også bede om den direkte: "Omskriv denne tekst med anti-slop-dansk."

## Tjekket

`scripts/dansk-lint.py` kræver kun Python 3.10 eller nyere.

```sh
python3 scripts/dansk-lint.py README.md docs/*.md
echo "Det er vigtigt at bemærke, at løsningen er sømløs." | python3 scripts/dansk-lint.py
python3 scripts/dansk-lint.py --json --baseline 5 docs/guide.md
python3 scripts/dansk-lint.py --disable passiv,papirord tekst.md
python3 scripts/dansk-lint.py --selftest
```

Tjekket har to niveauer:

- **fejl**: semikolon, sætninger med mere end 25 ord, AI-floskler, hype-ord, oversatte vendinger, substantivsyge og synonymrotation.
- **råd**: passiv, papirord, sætningsforlængere, lange sammensatte ord og konstrueret kontrast.

Exitkoden er 1, når der er flere fejl end `--baseline` (standard 0). Råd får aldrig tjekket til at fejle. Tjekket springer kodeblokke, kode i backticks og URL'er over.

Tjekket markerer aldrig forbehold som "måske", "muligvis" eller "kan have fejlet". Forbehold er indhold. Et tjek, som presser forbehold ud af teksten, ændrer påstandene.

Tjekket bruger regulære udtryk og har ingen ordbog. Se "Det, som tjekket ikke kan" i `references/kilder.md`.

Filerne i denne mappe citerer de mønstre, som de forbyder. Derfor giver tjekket fund i `SKILL.md` og i filerne i `references/` og `examples/`.

## Licens

MIT. Se `LICENSE`.

ASD-STE100 tilhører ASD. Du må ikke gengive standarden uden tilladelse fra ASD. Denne skill gengiver ikke standardens tekst eller ordbog.
