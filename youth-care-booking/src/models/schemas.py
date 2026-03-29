"""
Datamodellen voor Jeugdzorg met Verblijf — Centraal Dataplatform.

Alle modellen zijn gebaseerd op de business glossary en GGM-mapping.
Klantperspectief: deze modellen bepalen welke informatie beschikbaar is
om jeugdigen snel op de juiste plek te krijgen.
"""

from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, Field


class TypeVerblijf(str, Enum):
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
    totale_capaciteit: int = Field(..., ge=0)
    type_verblijf: TypeVerblijf
    leeftijd_van: int = Field(..., ge=0, le=23)
    leeftijd_tot: int = Field(..., ge=0, le=23)


class BezettingAanlevering(BaseModel):
    """Periodieke aanlevering van bezettingsdata door een aanbieder.

    Klantperspectief: deze data bepaalt of er plek is voor een jeugdige.
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


class BezettingGeanonimiseerd(BaseModel):
    """Geanonimiseerde bezettingsdata voor dashboards.

    Klantperspectief: dit is wat gemeenten zien als ze zoeken naar een plek.
    """

    regio_code: str
    locatie_pseudo_id: str  # Gepseudonimiseerd
    peildatum: date
    totale_capaciteit: int
    bezette_plekken: int
    beschikbare_plekken: int
    bezettingsgraad_pct: float = Field(..., ge=0, le=100)
    wachtlijst_aantal: int
    type_verblijf: TypeVerblijf
    zorgzwaarte: Zorgzwaarte | None
    leeftijd_van: int
    leeftijd_tot: int


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
