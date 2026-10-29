# Ordliste

Denne liste er skrevet til skillen. Den bygger på Dansk Sprognævns råd om klarsprog (se `kilder.md`). Den er ikke en officiel liste over godkendte ord.

Kolonnen "Tjek" viser, om `scripts/dansk-lint.py` finder ordet, og på hvilket niveau.

## Papirord

Papirord gør teksten formel og skaber afstand. Brug hverdagsordet.

| Skriv ikke | Skriv | Tjek |
|---|---|---|
| såfremt | hvis | råd |
| endvidere, ydermere | også, desuden | råd |
| hvorledes | hvordan | råd |
| hvorvidt | om | råd |
| vedrørende | om | råd |
| i henhold til, i medfør af | efter | råd |
| med henblik på | for at | råd |
| under henvisning til | (slet), eller "fordi" | råd |
| forefindes | findes, er | råd |
| erholde | få | råd |
| fremsende | sende | råd |
| foranledige | sørge for | råd |
| påbegynde | begynde | råd |
| iværksætte | starte, sætte i gang | råd |
| tilstræbe | prøve, have som mål | råd |
| nærværende | denne, dette | råd |
| ovennævnte, ovenstående, nedenstående | denne, disse, eller navnet på tingen | råd |
| efterfølgende | senere, bagefter, derefter | råd |
| pågældende | denne, eller navnet på tingen | råd |
| anvende, benytte | bruge | synonymrotation |

## Substantivsyge

Brug verbet i stedet for navneordet. Navneord på -ing, -else, -tion og -sion gemmer handlingen og den, der handler.

| Skriv ikke | Skriv | Tjek |
|---|---|---|
| foretage en vurdering af | vurdere | fejl |
| foretage en gennemgang af | gennemgå | fejl |
| gennemføre en installation af | installere | fejl |
| udføre en opdatering af | opdatere | fejl |
| træffe en beslutning om | beslutte | fejl |
| undersøgelsen fandt sted | (navn) undersøgte | fejl |
| rette henvendelse til | henvende sig til, kontakte | – |
| til brug for vurdering af | for at vurdere | – |
| med henblik på afklaring af | for at afklare | – |

## Engelske vendinger oversat ord for ord

| Skriv ikke | Skriv | Engelsk kilde | Tjek |
|---|---|---|---|
| række ud til | kontakte, skrive til | reach out to | fejl |
| adressere (et problem) | løse, tage fat på, behandle | address | fejl |
| på daglig basis | dagligt, hver dag | on a daily basis | fejl |
| levere på | opfylde, holde | deliver on | fejl |
| tage ejerskab | tage ansvar | take ownership | fejl |
| eksekvere | udføre, gennemføre | execute | fejl |
| i sidste ende | til sidst, (slet) | at the end of the day | fejl |
| ved dagens afslutning | til sidst, (slet) | at the end of the day | fejl |
| gøre en forskel | (skriv den konkrete virkning) | make a difference | fejl |
| dykke ned i | undersøge, læse, se på | dive into | fejl |
| navigere i landskabet | (skriv den konkrete handling) | navigate the landscape | fejl |
| frigøre potentialet | (skriv den konkrete virkning) | unlock the potential | fejl |
| tage det til næste niveau | forbedre | take it to the next level | fejl |

"Give mening" står ikke på listen. Vendingen kommer fra engelsk, men den er almindelig på dansk i dag, og den er ikke uklar.

## AI-floskler

Floskler fylder uden at sige noget. Slet dem, og skriv påstanden direkte.

| Skriv ikke | Gør i stedet | Tjek |
|---|---|---|
| Det er vigtigt at bemærke, at ... | Skriv påstanden. | fejl |
| Det er værd at nævne, at ... | Skriv påstanden. | fejl |
| I nutidens digitale verden ... | Slet. | fejl |
| I en verden, hvor ... | Slet. | fejl |
| ... spiller en afgørende rolle | Skriv, hvad det gør. | fejl |
| et væld af, en bred vifte af | mange, eller tallet | fejl |
| Uanset om du er X eller Y ... | Skriv, hvem teksten er til. | fejl |
| Godt spørgsmål! | Slet. | fejl |
| Jeg håber, det hjælper. | Slet. | fejl |
| Sig endelig til, hvis ... | Slet. | fejl |
| Det er ikke bare X – det er Y. | Skriv, hvad det er. | råd |
| Samlet set, Overordnet set, Afslutningsvis | Slet, hvis afsnittet kun gentager teksten. | – |

## Hype-ord

Hype-ord påstår en kvalitet uden at vise den. Slet ordet, eller skriv målingen.

| Skriv ikke | Skriv i stedet (eksempel) | Tjek |
|---|---|---|
| sømløs, gnidningsfri, problemfri | (slet), eller "uden manuelle trin" | fejl |
| robust | "fortsætter, når en node fejler" | fejl |
| kraftfuld | (skriv, hvad værktøjet kan) | fejl |
| lynhurtig | "svarer på under 100 ms" | fejl |
| banebrydende, revolutionerende | (slet) | fejl |
| skræddersyet | "tilpasset til X" | fejl |
| state-of-the-art, cutting-edge | (slet), eller versionen | fejl |
| i verdensklasse, enestående, uovertruffen | (slet) | fejl |

## Synonymgrupper

`scripts/dansk-lint.py` viser en fejl, når en tekst bruger mere end ét ord fra den samme gruppe.

| Gruppe |
|---|
| tjekke, kontrollere, verificere, validere, bekræfte |
| slette, fjerne |
| starte, begynde, påbegynde, igangsætte, initiere |
| stoppe, standse, terminere |
| vise, fremvise |
| bruge, anvende, benytte, udnytte |
| reparere, fikse |
| sende, fremsende |
| hente, indhente, fremskaffe |
| ændre, modificere |
