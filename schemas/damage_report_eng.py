from typing import List
from pydantic import BaseModel, Field, ConfigDict


class WorkItem(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "description": "Represents a single actionable work item with quantity, unit, confidence, and optional pricing."
        }
    )

    designation: str = Field(..., description="Short label or name of the work item.")
    description: str = Field(..., description="Detailed explanation of the work to be carried out.")
    quantite: float = Field(..., ge=0, description="Quantity of work to be performed.")
    unite: str = Field(..., description="Unit of measurement for the quantity, for example m2, m3, unit, or linear meter.")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score of the extracted or estimated work item, between 0 and 1.")
    unit_price: float = Field(0.0, ge=0, description="Unit price associated with the work item.")


class LotWork(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "description": "Represents a work trade or lot containing multiple work items."
        }
    )

    lot: str = Field(..., description="Category or trade of work, for example painting, plumbing, flooring, or electricity.")
    items: List[WorkItem] = Field(..., description="List of work items belonging to this trade or lot.")


class ZoneWork(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "description": "Represents a specific zone inside a room where work is required."
        }
    )

    zone: str = Field(..., description="Specific area inside the room or piece where the work applies, for example wall, ceiling, floor, or window area.")
    travaux: List[LotWork] = Field(..., description="List of work lots identified for this zone.")


class PieceReport(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "description": "Represents all repair work identified inside a given room or property section."
        }
    )

    piece: str = Field(..., description="Name of the room or section of the property, for example kitchen, bathroom, or living room.")
    zones: List[ZoneWork] = Field(..., description="List of zones within the room and their associated work.")


class MultiDamageReport(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "description": "Top-level structured report containing all damaged rooms, zones, and associated work items."
        }
    )

    pieces: List[PieceReport] = Field(..., description="Complete list of rooms or property sections included in the damage report.")