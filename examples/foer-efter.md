# Eksempler før og efter

Eksemplerne er skrevet til denne skill. Hvert eksempel viser niveauet, originalen, omskrivningen og de regler, som originalen brød.

## 1. Fejlbesked (Streng)

**Før**

> Der opstod desværre en uventet fejl under behandlingen af din anmodning; prøv venligst igen senere, eller ræk ud til supporten, såfremt problemet fortsætter.

**Efter**

> Vi kunne ikke behandle din anmodning. Prøv igen senere. Kontakt supporten, hvis fejlen sker igen.

**Regler:** semikolon, "ræk ud til" (oversat vending), "såfremt" (papirord), "under behandlingen af" (substantivsyge), "der opstod" uden den, der handler.

Omskrivningen beholder "senere". Skriv kun en ventetid, fx "om 5 minutter", hvis kilden har den.

## 2. Værktøjsbeskrivelse til en agent (Streng)

**Før**

> Dette kraftfulde værktøj gør det muligt for agenten at foretage en sømløs søgning i alle filer i projektet, hvilket sikrer, at relevante resultater bliver fundet hurtigt og effektivt.

**Efter**

> Søger efter tekst i alle filer i projektet. Giver filnavn, linjenummer og den linje, som matcher.

**Regler:** "kraftfulde" og "sømløs" (hype-ord), "foretage en søgning" (substantivsyge), ", hvilket" (sætningsforlænger), "bliver fundet" (passiv), "hurtigt og effektivt" (påstand uden måling).

## 3. Instruktion til en agent (Streng)

**Før**

> Du skal tjekke konfigurationen og verificere, at porten er korrekt, og derefter bekræfte, at serveren kører, inden du går videre.

**Efter**

> 1. Tjek, at porten i konfigurationen er 8080.
> 2. Tjek, at serveren kører.
> 3. Gå videre til næste trin.

**Regler:** synonymrotation ("tjekke", "verificere", "bekræfte" for den samme handling), flere instruktioner i én sætning, et forløb med 3 trin uden liste.

"8080" er et eksempel. Originalen siger kun "korrekt". Brug den port, som opgaven kræver. Hvis du ikke kender den, så skriv "Tjek, at porten i konfigurationen er korrekt."

## 4. Statusbesked med forbehold (Streng)

**Før**

> Det er vigtigt at bemærke, at buildet potentielt muligvis kan være fejlet på grund af netværket.

**Efter**

> Buildet fejlede muligvis på grund af netværket.

**Regler:** tom floskel ("Det er vigtigt at bemærke"), stablede forbehold ("potentielt muligvis kan").

Omskrivningen beholder ét forbehold ("muligvis"). Den skriver ikke "Buildet fejlede på grund af netværket". Det ville være en anden påstand.

## 5. README (Let)

**Før**

> I nutidens hurtige digitale verden er det afgørende at have et robust værktøj. Vores CLI `foo` er ikke bare et program – det er en partner, der hjælper dig med at frigøre dit fulde potentiale og tage din workflow til næste niveau. Det opretter projekter og kører testene for dig.

**Efter**

> `foo` er et kommandolinjeværktøj. Det opretter projekter og kører testene.

**Regler:** "I nutidens hurtige digitale verden" (floskel), "robust" (hype-ord), "ikke bare ... – det er" (konstrueret kontrast), "frigøre dit fulde potentiale" og "til næste niveau" (billedsprog fra engelsk).

Kun den sidste sætning i originalen har indhold. Omskrivningen beholder den og sletter resten. Hvis originalen ikke sagde, hvad værktøjet gør, så måtte du ikke skrive det. Sig i stedet, at teksten ikke har noget indhold (se Grænser i `SKILL.md`).

## 6. Commit-besked (Let)

**Før**

> Foretog en gennemgang og opdatering af installationsscriptet med henblik på at adressere problemet med manglende tilladelser.

**Efter**

> Ret de manglende tilladelser i installationsscriptet

**Regler:** "Foretog en gennemgang og opdatering" (substantivsyge), "med henblik på" (papirord), "adressere" (oversat vending).

## 7. Tekst, som allerede følger reglerne

**Før**

> Kør `make test`. Hvis en test fejler, så læs loggen i `build/test.log`.

**Efter**

> (Ingen ændring. Teksten følger reglerne.)
