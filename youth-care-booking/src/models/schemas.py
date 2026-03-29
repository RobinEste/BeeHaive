"""
Datamodellen voor Noordje op weg naar thuis — Dataplatform.

Alle modellen zijn gebaseerd op de business glossary, informatiebehoefte
en GGM-mapping. Klantperspectief: deze modellen bepalen welke informatie
beschikbaar is om jongeren zo dicht mogelijk bij thuis te laten wonen.
"""

from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, Field


# --- Enums ---


class TypeVerblijf(str, Enum):
    """Type verblijfsvorm conform codelijst."""

    PLEEGZORG = "PLG"
    GEZINSHUIS = "GZH"
    RESIDENTIEEL = "RES"
    GESLOTEN = "GJJ"
    CRISISOPVANG = "CRS"
    KAMERTRAINING = "KTW"


class Zorgzwaarte(str, Enum):
    LICHT = "ZZ1"
    REGULIER = "ZZ2"
    INTENSIEF = "ZZ3"
    HOOG_SPECIALISTISCH = "ZZ4"


class Frequentie(str, Enum):
    DAGELIJKS = "dag"
    WEKELIJKS = "week"
    MAANDELIJKS = "maand"


class TypeMaatregel(str, Enum):
    """Juridische grondslag voor de jeugdhulp."""

    VRIJWILLIG = "vrijwillig"
    BESCHERMINGSMAATREGEL = "beschermingsmaatregel"  # OTS, voogdij
    JEUGDRECLASSERING = "jeugdreclassering"


class TypePlaatsing(str, Enum):
    """Classificatie van een plaatsing naar aanleiding."""

    NIEUW = "nieuw"
    HERNIEUWD = "hernieuwd"
    OVERPLAATSING = "overplaatsing"
    SPOED = "spoed"
    REGULIER = "regulier"


class TypeVerwijzer(str, Enum):
    """Wie heeft de jongere verwezen naar jeugdhulp met verblijf?"""

    HUISARTS = "huisarts"
    WIJKTEAM = "wijkteam"
    GI = "gecertificeerde_instelling"
    KINDERRECHTER = "kinderrechter"
    JEUGDRECLASSERING = "jeugdreclassering"


# --- Organisatie ---


class Aanbieder(BaseModel):
    """Organisatie die jeugdhulp met verblijf levert."""

    agb_code: str = Field(..., description="AGB-code van de aanbieder", pattern=r"^\d{8}$")
    naam: str
    kvk_nummer: str | None = Field(None, pattern=r"^\d{8}$")
    regio_code: str
    type_zorg: list[TypeVerblijf]


class Locatie(BaseModel):
    """Fysieke verblijfslocatie van een aanbieder."""

    locatie_id: str
    aanbieder_agb: str
    naam: str
    straat: str
    postcode: str = Field(..., pattern=r"^\d{4}[A-Z]{2}$")
    plaats: str
    gemeente_code: str = Field(..., description="CBS gemeentecode (4 cijfers)")
    totale_capaciteit: int = Field(..., ge=0)
    type_verblijf: TypeVerblijf
    leeftijd_van: int = Field(..., ge=0, le=23)
    leeftijd_tot: int = Field(..., ge=0, le=23)
    kleinschalig: bool = Field(False, description="Kleinschalige woonvorm (≤8 plekken)")


# --- Plaatsingen (Prio 1) ---


class Plaatsing(BaseModel):
    """Een plaatsing van een jongere bij een zorgaanbieder.

    Klantperspectief: "De beslissing waar ik ga wonen voor mijn hulp."
    """

    plaatsing_id: str
    pseudo_id: str = Field(..., description="Gepseudonimiseerd persoons-ID")
    aanbieder_agb: str
    locatie_id: str
    type_plaatsing: TypePlaatsing
    type_verblijf: TypeVerblijf
    maatregel: TypeMaatregel
    verwijzer: TypeVerwijzer
    startdatum: date
    einddatum: date | None = None
    verwachte_duur_dagen: int | None = Field(None, ge=0)
    woonplaats_jongere: str | None = Field(None, description="Gemeente van herkomst")
    gemeente_code_herkomst: str | None = None
    aanvullende_trajecten: list[str] = Field(
        default_factory=list,
        description="Productcodes van aanvullende behandeling/begeleiding naast verblijf",
    )


class Voorgeschiedenis(BaseModel):
    """Eerdere jeugdhulptrajecten van een jongere (stapeling).

    Klantperspectief: "Ik heb al op veel plekken gewoond — zien ze dat ook?"
    """

    pseudo_id: str
    trajecten: list["Traject"]
    totaal_aantal_trajecten: int = Field(..., ge=0)
    totaal_aantal_aanbieders: int = Field(..., ge=0)


class Traject(BaseModel):
    """Eén jeugdhulptraject in de voorgeschiedenis."""

    aanbieder_agb: str
    aanbieder_naam: str | None = None
    type_zorg: str
    type_verblijf: TypeVerblijf | None = None
    startdatum: date
    einddatum: date | None = None
    duur_dagen: int | None = None


# --- Bezetting en Beschikbaarheid ---


class BezettingAanlevering(BaseModel):
    """Periodieke aanlevering van bezettingsdata door een aanbieder.

    Klantperspectief: deze data bepaalt of er plek is voor een jongere.
    """

    aanbieder_agb: str
    locatie_id: str
    peildatum: date
    frequentie: Frequentie
    totale_capaciteit: int = Field(..., ge=0)
    bezette_plekken: int = Field(..., ge=0)
    beschikbare_plekken: int = Field(..., ge=0)
    wachtlijst_aantal: int = Field(0, ge=0)
    gemiddelde_wachttijd_dagen: int | None = Field(None, ge=0)
    type_verblijf: TypeVerblijf
    zorgzwaarte: Zorgzwaarte | None = None
    opmerkingen: str | None = None
    aangeleverd_op: datetime = Field(default_factory=datetime.now)


class InUitstroom(BaseModel):
    """Instroom/uitstroom per locatie per periode.

    Klantperspectief: "Hoeveel jongeren komen en gaan — wordt er plek vrij?"
    """

    aanbieder_agb: str
    locatie_id: str
    periode_start: date
    periode_eind: date
    instroom: int = Field(..., ge=0)
    uitstroom: int = Field(..., ge=0)
    type_verblijf: TypeVerblijf


# --- Dashboard (geanonimiseerd) ---


class DashboardPlaatsingen(BaseModel):
    """Geanonimiseerde plaatsingsdata voor dashboards.

    Klantperspectief: dit is wat beleidsmakers zien om betere besluiten te nemen.
    """

    regio_code: str
    gemeente_code: str | None = None
    peildatum: date
    type_verblijf: TypeVerblijf
    maatregel: TypeMaatregel | None = None
    type_plaatsing: TypePlaatsing | None = None
    aantal_plaatsingen: int = Field(..., ge=0)
    aantal_gesloten: int = Field(0, ge=0, description="Aantal gesloten plaatsingen")
    aantal_kleinschalig: int = Field(0, ge=0, description="Aantal in kleinschalige woonvormen")
    aantal_buiten_regio: int = Field(0, ge=0, description="Geplaatst buiten eigen regio")
    gemiddelde_duur_dagen: float | None = None
    instroom: int = Field(0, ge=0)
    uitstroom: int = Field(0, ge=0)


class DashboardBeschikbaarheid(BaseModel):
    """Geanonimiseerde beschikbaarheidsdata voor dashboards."""

    regio_code: str
    peildatum: date
    type_verblijf: TypeVerblijf
    totale_capaciteit: int
    bezette_plekken: int
    beschikbare_plekken: int
    bezettingsgraad_pct: float = Field(..., ge=0, le=100)
    wachtlijst_totaal: int
    aantal_locaties: int
    aantal_kleinschalig: int


# --- AI Data Quality ---


class DataKwaliteitScore(BaseModel):
    """Resultaat van de AI-agent datakwaliteitsbeoordeling."""

    aanlevering_id: str
    aanbieder_agb: str
    peildatum: date
    overall_score: float = Field(..., ge=0, le=1)
    compleetheid: float = Field(..., ge=0, le=1, description="Percentage ingevulde velden")
    consistentie: float = Field(..., ge=0, le=1, description="Klopt bezet + vrij = totaal?")
    tijdigheid: float = Field(..., ge=0, le=1, description="Op tijd aangeleverd?")
    plausibiliteit: float = Field(..., ge=0, le=1, description="Vallen waarden binnen verwachte ranges?")
    signalen: list[str] = Field(default_factory=list)
    aanbevelingen: list[str] = Field(default_factory=list)
