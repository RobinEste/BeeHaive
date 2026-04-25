# KNW-2026-055: Wetenschappelijke claims toetsen op auteurs-positie, niet alleen feitelijkheid

> **Categorie:** process
> **Datum:** 2026-04-25
> **Sessie-context:** BB_01 Knowledge tweede lees-review — Robin pushte terug op de Kahneman & Klein-paragraaf met domeinkennis: "Maar klein en kahneman zeiden toch ook dat intuïtie nooit vertrouwd kan worden?"
> **Relevantie:** hoog

## Inzicht

AI-assistentie heeft de neiging om wetenschappelijke claims framing-positief te presenteren (rehabilitatief, oplossings-gericht), terwijl de bredere positie van de auteur(s) vaak skeptischer is dan de losse claim suggereert. Bij wetenschappelijke argumenten in content moet niet alleen worden gecontroleerd of de claim feitelijk klopt, maar ook of de framing de bredere positie van de auteur eerlijk weergeeft. De feitelijke claim kan technisch correct zijn én tegelijk de boodschap van het paper verraden.

## Context

In BB_01 Knowledge stond een paragraaf over Kahneman & Klein (2009) *"Conditions for Intuitive Expertise: A Failure to Disagree"*. De tekst zei: *"Kahneman en Klein onderzochten wanneer professionele intuïtie wél vertrouwd kan worden. Hun antwoord: alleen als twee voorwaarden allebei gelden."* Robin pushte terug.

Bij verificatie bleek de claim technisch correct (de twee voorwaarden — high-validity environment + adequate opportunity to learn — komen direct uit het paper), maar de framing miste essentiële context:

1. Het paper is een **verzoening** tussen Klein (NDM-traditie, intuïtie werkt soms) en Kahneman (heuristics-and-biases, intuïtie meestal onbetrouwbaar). De titel *"A Failure to Disagree"* verraadt dit: twee posities die elkaar niet kunnen weerleggen, maar ook niet kunnen poetsen.
2. Kahneman's bredere werk (*Thinking Fast and Slow*, *Noise*) is consistent skeptisch over intuïtie in de meeste professionele contexten.
3. De twee voorwaarden zijn in de meeste beroepen NIET vervuld. De claim "intuïtie kan worden vertrouwd onder voorwaarden" is in de praktijk een uitzondering, niet een regel.

De aangescherpte versie noemt nu expliciet: het paper is een verzoening, Kahneman bleef daarna scherper dan Klein, en de voorwaarden zijn in de meeste contexten niet vervuld.

## Geleerd

### Wat werkte
- Robin's pushback met domeinkennis ("zeiden ze niet dat intuïtie nooit vertrouwd kan worden?") leidde tot expliciete verificatie van de paper-context, niet alleen de losse claim.
- AI's eigen erkenning dat de claim technisch klopt maar de framing eenzijdig was — gevolgd door een herschrijving die beide kanten van het paper toonde.
- De aangescherpte tekst werd inhoudelijk *sterker* (meer spanning, scherpere boodschap voor Knowledge), niet zwakker, door de skepsis te integreren.

### Wat niet werkte
- AI presenteerde de claim als zelfstandige regel zonder de auteurs-skepsis die context geeft.
- Het paper-citaat ondersteunde technisch de bewering, maar de kop ("De twee voorwaarden waaronder intuïtie betrouwbaar is") las als rehabilitatie van intuïtie.
- Vertrouwen op één geciteerd paper, in plaats van te vragen "wat is de bredere positie van deze auteur?"

### Waarom
LLMs trainen op samenvattingen en losse claims uit papers, niet altijd op de bredere debatpositie van de auteur. Een claim als "Kahneman & Klein zeggen dat intuïtie betrouwbaar is onder X en Y" leeft als zelfstandige feiten-eenheid in het model; de meta-context (Kahneman's blijvende skepsis, Klein's tegenpositie, het reconciliatie-karakter van het paper) komt minder snel boven. De positief-framing-bias is bovendien sterk in instructie-getrainde modellen: een paper uitleggen voelt als een vraag om een nuttige, oplossings-gerichte samenvatting te geven.

## Toepassing

Bij content waarin een wetenschappelijke claim de boodschap draagt:

1. **Vraag actief naar de auteurs-positie** — niet alleen "klopt deze claim?" maar "wat was de bredere positie van deze auteur(s)?"
2. **Bij papers met verzoenende of contrast-titels** ("Failure to Disagree", "Reconciling X and Y", "A debate between..."): de claim is een verzoening, niet een unieke positie. Behandel de tegenpositie expliciet.
3. **Bij conditional claims** ("X kan vertrouwd worden ALS Y"): controleer of Y zelden of vaak vervuld is. Dat verandert de boodschap fundamenteel.
4. **Behandel domeinexperts als primaire tegen-check.** Robin's "wacht, klopt dat wel?" was de trigger. Als hun pushback niet door één citaat wordt overtuigd, vertrouw hun mens-laag-kennis en herzie de framing.
5. **Specifiek voor BeeHaive content**: bij wetenschappelijke fundering van een Building Block, schrijf de spanning expliciet uit — "auteur X stelde Y, maar bleef tegelijk skeptisch over Z". Dat maakt de boodschap voor de lezer scherper, niet zwakker.
