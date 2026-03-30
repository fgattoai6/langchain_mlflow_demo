
# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class WorkItem:
    designation: str
    description: str
    quantite: float
    unite: str
    confidence: float # can't followed by default valued variable that is unit_price so putting before unit_price
    unit_price: float = 0.0


@dataclass
class LotWork:
    lot: str
    items: List[WorkItem]


@dataclass
class ZoneWork:
    zone: str
    travaux: List[LotWork]


@dataclass
class PieceReport:
    piece: str
    zones: List[ZoneWork]


@dataclass
class MultiDamageReport:
    pieces: List[PieceReport]