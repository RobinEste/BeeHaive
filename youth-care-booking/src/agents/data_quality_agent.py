"""
AI Agent voor Datakwaliteitsbeoordeling — Jeugdzorg met Verblijf.

Deze agent beoordeelt de kwaliteit van aangeleverde data op basis van:
1. Procesbeschrijvingen (hoe zou de data eruit moeten zien?)
2. Transcripties (wat kan er misgaan in de praktijk?)
3. Business glossary (kloppen de definities?)
4. Historische patronen (wijkt het af van eerdere aanleveringen?)

Klantperspectief: slechte datakwaliteit betekent dat een jeugdige
misschien een plek mist die er wel is, of verwezen wordt naar een
instelling die eigenlijk vol zit.
"""

from datetime import date

from ..models.schemas import (
    BezettingAanlevering,
    DataKwaliteitScore,
)

SYSTEM_PROMPT = """\
Je bent een datakwaliteits-agent voor het Jeugdzorg met Verblijf dataplatform.

Je beoordeelt aangeleverde bezettingsdata van jeugdzorgaanbieders op vier dimensies:
1. Compleetheid — zijn alle verplichte velden ingevuld?
2. Consistentie — klopt de interne logica (bezet + vrij = totaal)?
3. Tijdigheid — is de data op tijd aangeleverd?
4. Plausibiliteit — vallen waarden binnen verwachte ranges?

Gebruik je kennis van de procesbeschrijvingen en transcripties om context te geven.
Bijvoorbeeld: als een aanbieder wachtlijstdata mist, en de transcriptie vertelt
dat ze geen formele wachtlijst bijhouden, is dat een bekend probleem dat anders
gewogen moet worden dan een onverklaarbare omissie.

Geef concrete, actionable aanbevelingen. Vermijd vage feedback.
"""


def check_compleetheid(aanlevering: BezettingAanlevering) -> tuple[float, list[str]]:
    """Controleer of alle verwachte velden zijn ingevuld."""
    signalen = []
    velden_totaal = 0
    velden_ingevuld = 0

    verplicht = [
        ("aanbieder_agb", aanlevering.aanbieder_agb),
        ("locatie_id", aanlevering.locatie_id),
        ("peildatum", aanlevering.peildatum),
        ("totale_capaciteit", aanlevering.totale_capaciteit),
        ("bezette_plekken", aanlevering.bezette_plekken),
        ("beschikbare_plekken", aanlevering.beschikbare_plekken),
        ("type_verblijf", aanlevering.type_verblijf),
    ]

    optioneel = [
        ("wachtlijst_aantal", aanlevering.wachtlijst_aantal),
        ("gemiddelde_wachttijd_dagen", aanlevering.gemiddelde_wachttijd_dagen),
        ("zorgzwaarte", aanlevering.zorgzwaarte),
    ]

    for naam, waarde in verplicht:
        velden_totaal += 1
        if waarde is not None:
            velden_ingevuld += 1
        else:
            signalen.append(f"Verplicht veld '{naam}' ontbreekt")

    for naam, waarde in optioneel:
        velden_totaal += 1
        if waarde is not None:
            velden_ingevuld += 1
        else:
            signalen.append(f"Optioneel veld '{naam}' niet ingevuld")

    score = velden_ingevuld / velden_totaal if velden_totaal > 0 else 0
    return score, signalen


def check_consistentie(aanlevering: BezettingAanlevering) -> tuple[float, list[str]]:
    """Controleer interne logica van de aanlevering."""
    signalen = []
    checks_totaal = 0
    checks_ok = 0

    # Check: bezet + vrij = totaal
    checks_totaal += 1
    som = aanlevering.bezette_plekken + aanlevering.beschikbare_plekken
    if som == aanlevering.totale_capaciteit:
        checks_ok += 1
    else:
        signalen.append(
            f"Bezet ({aanlevering.bezette_plekken}) + vrij "
            f"({aanlevering.beschikbare_plekken}) = {som}, "
            f"maar totaal = {aanlevering.totale_capaciteit}"
        )

    # Check: bezetting niet hoger dan capaciteit
    checks_totaal += 1
    if aanlevering.bezette_plekken <= aanlevering.totale_capaciteit:
        checks_ok += 1
    else:
        signalen.append(
            f"Bezetting ({aanlevering.bezette_plekken}) hoger dan "
            f"capaciteit ({aanlevering.totale_capaciteit})"
        )

    # Check: geen negatieve beschikbaarheid
    checks_totaal += 1
    if aanlevering.beschikbare_plekken >= 0:
        checks_ok += 1
    else:
        signalen.append("Beschikbare plekken is negatief")

    score = checks_ok / checks_totaal if checks_totaal > 0 else 0
    return score, signalen


def check_tijdigheid(aanlevering: BezettingAanlevering, verwachte_datum: date) -> tuple[float, list[str]]:
    """Controleer of de aanlevering op tijd is."""
    signalen = []
    dagen_verschil = (aanlevering.peildatum - verwachte_datum).days

    if dagen_verschil == 0:
        return 1.0, signalen
    elif abs(dagen_verschil) <= 1:
        signalen.append(f"Aanlevering {abs(dagen_verschil)} dag afwijking van schema")
        return 0.8, signalen
    elif abs(dagen_verschil) <= 7:
        signalen.append(f"Aanlevering {abs(dagen_verschil)} dagen afwijking van schema")
        return 0.5, signalen
    else:
        signalen.append(f"Aanlevering {abs(dagen_verschil)} dagen te laat/vroeg")
        return 0.2, signalen


def check_plausibiliteit(aanlevering: BezettingAanlevering) -> tuple[float, list[str]]:
    """Controleer of waarden binnen plausibele ranges vallen."""
    signalen = []
    checks_totaal = 0
    checks_ok = 0

    # Capaciteit: typisch 1-200 voor een locatie
    checks_totaal += 1
    if 1 <= aanlevering.totale_capaciteit <= 200:
        checks_ok += 1
    else:
        signalen.append(
            f"Capaciteit ({aanlevering.totale_capaciteit}) valt buiten "
            f"verwachte range (1-200)"
        )

    # Bezettingsgraad: alert bij >95% of <20%
    checks_totaal += 1
    if aanlevering.totale_capaciteit > 0:
        bezettingsgraad = aanlevering.bezette_plekken / aanlevering.totale_capaciteit
        if 0.2 <= bezettingsgraad <= 0.95:
            checks_ok += 1
        elif bezettingsgraad > 0.95:
            signalen.append(
                f"Bezettingsgraad {bezettingsgraad:.0%} — bijna vol, "
                f"controleer of dit klopt"
            )
            checks_ok += 0.5
        else:
            signalen.append(
                f"Bezettingsgraad {bezettingsgraad:.0%} — ongewoon laag"
            )
            checks_ok += 0.5

    # Wachttijd: alert bij >365 dagen
    checks_totaal += 1
    if aanlevering.gemiddelde_wachttijd_dagen is None:
        checks_ok += 0.5
        signalen.append("Geen wachttijd opgegeven")
    elif aanlevering.gemiddelde_wachttijd_dagen <= 365:
        checks_ok += 1
    else:
        signalen.append(
            f"Wachttijd {aanlevering.gemiddelde_wachttijd_dagen} dagen — ongewoon hoog"
        )

    score = checks_ok / checks_totaal if checks_totaal > 0 else 0
    return score, signalen


def beoordeel_aanlevering(
    aanlevering: BezettingAanlevering,
    verwachte_datum: date,
    aanlevering_id: str,
) -> DataKwaliteitScore:
    """Voer een volledige datakwaliteitsbeoordeling uit op een aanlevering."""
    compleetheid_score, compleetheid_signalen = check_compleetheid(aanlevering)
    consistentie_score, consistentie_signalen = check_consistentie(aanlevering)
    tijdigheid_score, tijdigheid_signalen = check_tijdigheid(aanlevering, verwachte_datum)
    plausibiliteit_score, plausibiliteit_signalen = check_plausibiliteit(aanlevering)

    alle_signalen = (
        compleetheid_signalen
        + consistentie_signalen
        + tijdigheid_signalen
        + plausibiliteit_signalen
    )

    # Gewogen gemiddelde: consistentie weegt zwaarder
    overall = (
        compleetheid_score * 0.2
        + consistentie_score * 0.35
        + tijdigheid_score * 0.15
        + plausibiliteit_score * 0.3
    )

    aanbevelingen = []
    if compleetheid_score < 0.8:
        aanbevelingen.append("Vul alle verplichte velden in bij de volgende aanlevering")
    if consistentie_score < 1.0:
        aanbevelingen.append("Controleer of bezet + vrij = totaal klopt")
    if tijdigheid_score < 0.8:
        aanbevelingen.append("Lever data aan op de afgesproken peildatum")
    if plausibiliteit_score < 0.8:
        aanbevelingen.append("Controleer opvallende waarden handmatig")

    return DataKwaliteitScore(
        aanlevering_id=aanlevering_id,
        aanbieder_agb=aanlevering.aanbieder_agb,
        peildatum=aanlevering.peildatum,
        overall_score=round(overall, 2),
        compleetheid=round(compleetheid_score, 2),
        consistentie=round(consistentie_score, 2),
        tijdigheid=round(tijdigheid_score, 2),
        plausibiliteit=round(plausibiliteit_score, 2),
        signalen=alle_signalen,
        aanbevelingen=aanbevelingen,
    )
