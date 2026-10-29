---
name: anti-slop-dansk
description: "Brug denne skill, når du skriver eller redigerer dansk tekst, som skal være klar, entydig og fri for AI-sprog: fejlbeskeder, logbeskeder, statusbeskeder, værktøjsbeskrivelser, instruktioner til agenter, systemprompter, README-filer, dokumentation, commit-beskeder og PR-beskrivelser. Brug den også, når en dansk tekst er tung, kancellistisk, oversat ord for ord fra engelsk eller lyder som en sprogmodel. Udløsere: klarsprog, skriv klart dansk, fjern AI-sprog, anti-slop, omskriv til enkelt dansk, Danish plain language, Danish anti-slop. Ikke til skønlitteratur eller reklametekst."
version: 0.1.0
---

# Klart dansk uden AI-sprog

Denne skill omskriver dansk tekst, så en læser kun kan forstå den på én måde. Læseren kan være et menneske, en sprogmodel, et oversættelsesprogram eller et andet system. Skillen fjerner også de mønstre, som afslører en tekst fra en sprogmodel ("AI-slop"): tomme floskler, hype-ord, engelske vendinger oversat ord for ord og konstrueret retorik.

Skillen bygger på to kilder:

- **ASD-STE100 Simplified Technical English** (Issue 9, 2025). Det er en standard fra luftfartsindustrien for engelsk teknisk tekst. Skillen bruger standardens principper for sætningsbygning: aktiv form, én instruktion pr. sætning, korte sætninger, ét ord for én betydning og ingen semikolon.
- **Dansk klarsprog**, især Dansk Sprognævns råd. Klarsprog giver de danske regler, som STE ikke har: substantivsyge, papirord, forvægt, sætningsforlængere og lange sammensatte ord.

Der findes ingen officiel dansk udgave af STE. Denne skill er derfor ikke en certificeret standard. Den er et værktøj til klar tekst. Ordlisterne er skrevet til denne skill. Skillen gengiver ikke ASD's ordbog. Se `references/kilder.md`.

## Hvornår skal du bruge skillen

- En tekst fra en agent (forklaring, instruktion, logbesked, værktøjsbeskrivelse) er tung, uklar eller kan forstås på flere måder.
- En anden agent, et oversættelsesprogram eller en læser med et andet modersmål skal læse teksten, og en misforståelse har en pris.
- Du skriver en prompt, en systembesked eller en værktøjsbeskrivelse på dansk.
- En dansk tekst lyder som en sprogmodel: "Det er vigtigt at bemærke", "sømløs", "dykke ned i", "række ud til".
- Brugeren beder om en sammenligning før og efter, med de regler, som teksten brød. Standardoutputtet er kun den omskrevne tekst (se Outputformat).

Brug ikke skillen til skønlitteratur, reklametekst eller tekst, hvor stemme og nuancer er formålet.

## To niveauer

Vælg et niveau, før du omskriver. Hvis brugeren ikke vælger, så vælg ud fra teksttypen. Nævn kun valget, hvis brugeren beder om regeltabellen.

**Streng** — procedurer, fejlbeskeder, logbeskeder, statusbeskeder, værktøjsbeskrivelser, instruktioner til agenter og sikkerhedstekst. Det vil sige tekst, hvor en forkert forståelse har en pris. Brug alle regler, også de faste længdegrænser og reglen om ét ord for én betydning.

**Let** — README-filer, dokumentation, PR-beskrivelser, commit-beskeder, ændringslogs og forklarende tekst. Brug alle reglerne for sætningsbygning og hele tjeklisten for AI-sprog. Brug reglerne for ordvalg som råd. Prosa må gerne variere ordene lidt og veksle mellem korte og længere sætninger, så længe ingen sætning er længere end 25 ord.

## Regler for sætningsbygning

| Regel | Skriv | Skriv ikke |
|---|---|---|
| Aktiv form | "Agenten sletter filen." | "Filen slettes (af agenten)." Brug kun passiv, når den handlende er ukendt eller uvæsentlig. |
| Nævn den, der handler | "Du skal udfylde formularen." | "Der skal udfyldes en formular." eller "Man skal udfylde formularen." |
| Én instruktion pr. sætning | "Åbn filen. Læs linje 3." | "Åbn filen, og læs linje 3, og kontrollér derefter, om den passer." |
| Sætningslængde | Højst 20 ord i instruktioner. Højst 25 ord i beskrivelser. | Lange sætninger med mange ledsætninger. |
| Hovedsagen først | "Vi afviser ansøgningen, fordi fristen er overskredet." | "Under hensyn til at fristen er overskredet, og at (...), afviser vi ansøgningen." (forvægt) |
| Ingen semikolon | Del sætningen i to sætninger. | Semikolon. Tankestreg er ikke forbudt, men den er ofte et tegn på, at sætningen skal deles. |
| Ingen sætningsforlængere | "Serveren svarede ikke. Derfor stoppede jobbet." | "Serveren svarede ikke, hvorfor jobbet stoppede." (også "idet", "hvilket", "hvoraf", "ligesom") |
| Få indskud | Skriv indskuddet som en ny sætning. | Lange parenteser eller indskud midt i sætningen. |
| Verber frem for navneord | "Vurder sagen." | "Foretag en vurdering af sagen." (substantivsyge: ord på -ing, -else, -tion) |
| Korte sammensatte ord | "mulighed for dispensation" | "dispensationsmulighed", især sammensætninger med tre led eller flere |
| Ingen udeladelser | Skriv grundled, udsagnsled og artikel, også når teksten bliver længere. | "Filer ikke sikkerhedskopieret slettes." Det er uklart, hvilke filer det gælder. |
| Behold forbehold | "Anmodningen kan have fejlet." forbliver "kan have fejlet". | Gør et forbehold til en kendsgerning ("Anmodningen fejlede."), eller tilføj en sikkerhed, som kilden ikke havde. |
| Afsnit | Ét emne pr. afsnit, højst 6 sætninger. | Afsnit med flere emner. |
| Lister til forløb | Brug en nummereret liste eller en punktliste til 3 trin eller betingelser eller flere. | Et forløb gemt i én lang sætning. |

### Tider

STE forbyder perfektum på engelsk. Den regel passer ikke til dansk. På dansk er perfektum normalt, når en handling har betydning nu: "Jobbet er færdigt" eller "Vi har modtaget din anmodning". Brug datid, når tidspunktet er fast: "Jobbet stoppede kl. 14.02." Lav ikke perfektum om, kun for at følge en regel.

## Regler for ordvalg

| Regel | Skriv | Skriv ikke |
|---|---|---|
| Ét ord, én betydning | Vælg ét verbum for én handling, og brug det hver gang (fx altid "tjek"). | Skift mellem "tjek", "kontrollér", "verificér" og "bekræft" for den samme handling. Læseren kan ikke se, om det er én handling eller fire. |
| Hverdagsord frem for papirord | "hvis", "også", "om", "sende", "begynde", "senere" | "såfremt", "endvidere", "hvorvidt", "fremsende", "påbegynde", "efterfølgende" |
| Danske vendinger frem for oversatte | "kontakte", "løse", "dagligt", "udføre" | "række ud til", "adressere", "på daglig basis", "eksekvere" |
| Fagord | Behold de nødvendige fagord. Forklar et fagord én gang, hvis det ikke er almindeligt dansk. | Fagord, som teksten aldrig forklarer. |
| Engelske IT-ord | Brug det ord, som læseren faktisk bruger (fx "commit", "pull request", "deploy"). Skift ikke mellem et engelsk og et dansk ord for den samme ting. | Tvungne fordanskninger, som læseren ikke kender, eller skift mellem "commit" og "indsendelse". |
| Pronomener | Gentag navneordet, hvis "den", "det" eller "de" kan pege på to ting. | "Kør scriptet på serveren, og genstart den." Hvad skal du genstarte? |

Den fulde ordliste er i `references/ordliste.md`.

## Tjekliste for AI-sprog

Disse mønstre gør tekst fra sprogmodeller svær at læse og let at genkende. Hvert mønster er mekanisk: du kan pege på det ord eller tegn, som bryder reglen. Søg efter alle mønstre, før du omskriver.

1. **Tomme floskler** — "Det er vigtigt at bemærke, at", "I nutidens digitale verden", "spiller en afgørende rolle", "et væld af". Ret: slet floskeln, og skriv påstanden direkte.
2. **Hype-ord** — sømløs, robust, kraftfuld, banebrydende, problemfri, skræddersyet, lynhurtig. Ret: slet ordet, eller skriv det tal, som ordet påstår ("svarer på under 100 ms").
3. **Billedsprog fra engelsk** — "dykke ned i", "navigere i landskabet", "frigøre potentialet", "tage det til næste niveau". Ret: brug det almindelige verbum (undersøge, læse, forbedre).
4. **Engelske vendinger oversat ord for ord** — "række ud til", "adressere et problem", "på daglig basis", "levere på", "tage ejerskab", "i sidste ende". Ret: brug den danske vending.
5. **Konstrueret retorik** — "Det er ikke bare X – det er Y", tre punkter uden grund, et retorisk spørgsmål før svaret. Ret: skriv påstanden én gang.
6. **Stablede forbehold** — "det kan potentielt muligvis hjælpe med at forbedre". Ret: skriv ét forbehold med den samme styrke, eller skriv påstanden.
7. **Synonymrotation** — den samme ting har flere navne ("brugeren", "kunden", "klienten"). Ret: vælg ét navn.
8. **Substantivsyge og passiv** — "Der er foretaget en gennemgang af indstillingerne." Ret: "Vi har gennemgået indstillingerne."
9. **Indpakning** — "Godt spørgsmål!" før svaret, en opsummering af det, som læseren lige har læst, og "Sig endelig til, hvis du har spørgsmål" til sidst. Ret: slet indpakningen.

## Fremgangsmåde

1. Vælg niveauet (Streng eller Let). Nævn kun valget, hvis brugeren beder om regeltabellen (se Outputformat).
2. Læs teksten én gang for at forstå den. Begynd ikke at omskrive, før du ved, hvad teksten stadig skal sige bagefter.
3. Gå teksten igennem sætning for sætning. Markér hvert brud på reglerne og hvert mønster fra tjeklisten. På niveauet Let skal du markere reglerne for ordvalg, men du behøver ikke at følge dem. Kør `scripts/dansk-lint.py` for et mekanisk første tjek (stdin eller filer, `--json` giver struktureret output). Tjekket markerer aldrig forbehold.
4. Omskriv hver markeret sætning, så bruddet forsvinder, og betydningen er nøjagtigt den samme. Hvis en omskrivning fjerner nødvendig præcision (en sikkerhedsbetingelse, en afgrænsning, et tal), så behold den længere formulering, og markér den.
   - **Kontrollér forbeholdene, før du vælger en omskrivning.** Ord som "måske", "muligvis", "kan", "ofte" og "sandsynligvis" viser forfatterens sikkerhed. Sikkerhed er indhold. En kortere sætning, som gør et forbehold til en kendsgerning, er ikke en forenkling. Den er en anden påstand.
   - Tilføj aldrig en kendsgerning, som kilden ikke har. Hvis en omskrivning bliver bedre, fordi den tilføjer en årsag, en hyppighed eller en mekanisme, så er den ikke længere en omskrivning.
5. Skriv den omskrevne tekst (se Outputformat). Behold valget af niveau og analysen for dig selv, medmindre brugeren beder om dem.
6. Hvis teksten allerede følger reglerne, så sig det. Lav ikke ændringer, som teksten ikke behøver.

## Outputformat

**Standard: kun den omskrevne tekst.** De fleste brugere vil have et resultat, som de kan indsætte direkte i en værktøjsbeskrivelse, en fejlbesked eller en prompt. Skriv den forenklede tekst alene. Tilføj ikke en indledning om skillen, en meddelelse om niveauet, et antal brud, en opsummering af ændringerne, en regeltabel eller et tilbud om at forklare mere.

Én tilføjelse er tilladt: Hvis du i trin 4 bevidst beholdt en længere formulering, så tilføj én linje efter teksten. Begynd linjen med `Beholdt:`, og nævn formuleringen og den præcision, som ville forsvinde. Udelad linjen, hvis der ikke er noget at nævne.

**Når brugeren beder om det: regeltabellen.** Når brugeren vil se begrundelsen ("vis forskellen", "hvilke regler brød den", "forklar ændringerne", "før og efter"), så skriv denne tabel i stedet:

```markdown
| Brudt regel | Original | Forenklet |
|---|---|---|
| Substantivsyge | "Vi foretager en vurdering af sagen." | "Vi vurderer sagen." |
| Oversat vending | "Vi rækker ud til dig." | "Vi kontakter dig." |

Niveau: Streng. 7 brud fundet.
```

Skriv efter tabellen én linje om det, som du bevidst ikke forenklede, og hvorfor (som regel: en forenkling ville fjerne nødvendig præcision).

## Grænser

**Skillen skal:**
- Omskrive tung eller uklar dansk tekst til korte, entydige sætninger i aktiv form.
- Som standard kun skrive den omskrevne tekst, og nævne reglerne, når brugeren beder om det.
- Beholde alle kendsgerninger, betingelser og afgrænsninger fra originalen.
- Beholde styrken af alle forbehold og ikke tilføje en påstand, som kilden ikke har.
- Foreslå en kort forklaring på et fagord, som teksten skal beholde.

**Skillen må ikke:**
- Påstå, at teksten følger en officiel standard. Der findes ingen officiel dansk STE.
- Forenkle skønlitteratur, reklametekst eller overbevisende tekst, hvor stemme og nuancer er formålet.
- Fjerne en sikkerhedsbetingelse, en undtagelse eller en afgrænsning uden at sige det, kun for at gøre en sætning kortere.
- Lave "kan have fejlet" om til "fejlede", eller "skyldes muligvis X" om til "skyldes X". Et tabt forbehold ændrer påstanden.
- Gøre tomt indhold sandt eller nyttigt. Skillen retter tekstens form, ikke dens indhold. Hvis teksten ikke har noget at sige, så sig det i stedet for at pudse den.
- Forkorte teksten, så den bliver uklar. Målet er ikke færre ord. Målet er, at teksten kun kan forstås på én måde. Stop, når sætningen er entydig, ikke når den er kortest.

## Flere ressourcer

- **`references/ordliste.md`** — papirord, oversatte vendinger, AI-floskler og hype-ord, med det danske ord, som du skal bruge i stedet.
- **`references/kilder.md`** — kilderne til reglerne og forskellene mellem STE og dansk klarsprog.
- **`examples/foer-efter.md`** — eksempler på omskrivninger før og efter.
- **`scripts/dansk-lint.py`** — deterministisk tjek uden eksterne pakker. Det tjekker semikolon, sætningslængde, AI-floskler, hype-ord, oversatte vendinger, substantivsyge og synonymrotation (fejl). Det tjekker også passiv, papirord, sætningsforlængere, lange sammensatte ord og konstrueret kontrast (råd). Exitkode 1, når der er flere fejl end `--baseline` (standard 0). Fund på niveauet råd får aldrig tjekket til at fejle. `--disable` slår regler fra. Tjekket markerer aldrig forbehold. `--selftest` kontrollerer, at "kan have fejlet" ikke giver et fund.
