# Kilder og forskelle

## Kilder

| Kilde | Hvad skillen bruger |
|---|---|
| ASD-STE100 Simplified Technical English, Issue 9 (januar 2025). [asd-ste100.org](https://www.asd-ste100.org/) | Principperne for sætningsbygning: aktiv form, én instruktion pr. sætning, højst 20 ord i procedurer og 25 ord i beskrivelser, ingen semikolon (regel 8.1), verber frem for navneord (regel 3.7), korte navneordsforbindelser, lister til forløb og ét ord for én betydning. |
| Dansk Sprognævn: *Håndbog i klarsprog*. [PDF](https://dsn.dk/wp-content/uploads/2021/01/Haandbog-i-klarsprog.pdf) | Aktiv frem for passiv, substantivsyge ("verbalsubstantivets tørre knitren"), forvægt, indskud, kancellismer, papirord og sammensætninger med tre led eller flere. |
| Dansk Sprognævn: *Sprogpolitik for Danmarks Domstole*. [PDF](https://dsn.dk/wp-content/uploads/2021/01/sprogpolitik-for-danmarks-domstole.pdf) | Gennemsnitligt 15–18 ord pr. sætning, sætningsforlængere ("idet", "hvilket", "hvorfor", "hvoraf", "ligesom"), passiv uden handlende og ord på -ing, -ion, -ende og -else. |
| Dansk Sprognævn: *Og uden omsvøb – tak!* [PDF](https://dsn.dk/wp-content/uploads/2021/01/og-uden-omsvoeb-tak.pdf) | En læservenlig sætning har sjældent mere end 26 ord. |
| Danmarks Evalueringsinstitut: *Sprogbrug og skrivetips*. [guide.eva.dk](https://guide.eva.dk/god-webkommunikation/sprogbrug) | "Du" frem for "man", aktive sætninger og korte sammensatte ord ("mulighed for dispensation", ikke "dispensationsmulighed"). |
| Dansk Sprognævn: *Komma*. [sproget.dk](https://sproget.dk/typiske-problemer/komma/) | Startkomma er valgfrit, men en tekst skal være konsekvent. Tjekket i denne skill markerer ikke kommaer. |

ASD-STE100 må ikke gengives uden skriftlig tilladelse fra ASD. Denne skill gengiver ikke standardens regeltekst eller ordbog. Den bruger kun principperne. Ordlisterne i `ordliste.md` er skrevet til denne skill.

## Forskelle mellem STE og dansk

| Emne | STE (engelsk) | Denne skill (dansk) |
|---|---|---|
| Perfektum | Forbudt ("we received", ikke "we have received"). | Tilladt. På dansk er perfektum normalt, når en handling har betydning nu. |
| Partikelverber (phrasal verbs) | Forbudt ("take off" → "remove"). | Tilladt. Partikelverber er normale på dansk ("slå op", "sætte i gang"). Skillen forbyder kun oversatte vendinger som "række ud til". |
| Godkendt ordbog | Omkring 900 godkendte ord med én betydning hver. | Ingen fast ordbog. Skillen bruger lister over ord, som du ikke skal bruge, og det danske ord, som du skal bruge i stedet. |
| Sammensatte ord | Højst 3 ord i en navneordsforbindelse. | Dansk skriver sammensatte ord i ét ord. Skillen anbefaler at dele sammensætninger med tre led eller flere. Tjekket markerer ord med 22 bogstaver eller flere. |
| Passiv | Brug aktiv form. | Brug aktiv form. Dansk har to passiver: s-passiv ("slettes") og blive-passiv ("bliver slettet"). Begge skjuler den, der handler. |
| "man" og "der"-sætninger | Ikke relevant. | Nævn den, der handler: "du", "vi" eller navnet. |
| Modalverber | "may" er ikke godkendt. STE bruger "can" eller "possibly". | Behold "kan", "måske" og "muligvis" med den samme styrke som i kilden. |

## Det, som tjekket ikke kan

`scripts/dansk-lint.py` bruger regulære udtryk. Det har ingen ordbog og ingen grammatisk analyse. Derfor:

- Det finder kun s-passiv efter et modalverbum ("skal udfyldes"), ikke "Filen slettes". Mange verber på -s er ikke passiv ("findes", "synes", "lykkes").
- Det kan ikke finde særskrivning ("data base" i stedet for "database").
- Det kan ikke se forskel på en instruktion og en beskrivelse. Derfor bruger det grænsen på 25 ord for alle sætninger.
- Det kan ikke kontrollere, at en omskrivning har den samme betydning som originalen, eller at et forbehold har den samme styrke.

Et resultat uden fund betyder kun, at tjekket ikke fandt de mønstre, som det kender.
