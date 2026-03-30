from typing import List
from pydantic import BaseModel, Field, ConfigDict


class WorkItem(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "description": "Représente un poste de travaux élémentaire avec quantité, unité, niveau de confiance et prix unitaire optionnel."
        }
    )

    designation: str = Field(
        ...,
        description="Intitulé court ou nom du poste de travaux."
    )
    description: str = Field(
        ...,
        description="Description détaillée des travaux à réaliser."
    )
    quantite: float = Field(
        ...,
        ge=0,
        description="Quantité de travaux à effectuer."
    )
    unite: str = Field(
        ...,
        description="Unité de mesure associée à la quantité, par exemple m², m³, unité ou mètre linéaire."
    )
    confidence: float = Field(
        ...,
        ge=0,
        le=1,
        description="Niveau de confiance de l’extraction ou de l’estimation du poste, compris entre 0 et 1."
    )
    unit_price: float = Field(
        0.0,
        ge=0,
        description="Prix unitaire associé au poste de travaux."
    )


class LotWork(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "description": "Représente un lot de travaux regroupant plusieurs postes d’intervention."
        }
    )

    lot: str = Field(
        ...,
        description="Catégorie ou corps d’état des travaux, par exemple peinture, plomberie, revêtement de sol ou électricité."
    )
    items: List[WorkItem] = Field(
        ...,
        description="Liste des postes de travaux appartenant à ce lot."
    )


class ZoneWork(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "description": "Représente une zone précise à l’intérieur d’une pièce où des travaux sont nécessaires."
        }
    )

    zone: str = Field(
        ...,
        description="Zone spécifique à l’intérieur de la pièce concernée, par exemple mur, plafond, sol ou menuiserie."
    )
    travaux: List[LotWork] = Field(
        ...,
        description="Liste des lots de travaux identifiés pour cette zone."
    )


class PieceReport(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "description": "Représente l’ensemble des travaux identifiés dans une pièce ou une partie du bien."
        }
    )

    piece: str = Field(
        ...,
        description="Nom de la pièce ou de la partie du bien, par exemple cuisine, salle de bain ou séjour."
    )
    zones: List[ZoneWork] = Field(
        ...,
        description="Liste des zones de la pièce avec les travaux associés."
    )


class MultiDamageReport(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "description": "Rapport structuré de niveau supérieur contenant l’ensemble des pièces endommagées, des zones concernées et des travaux associés."
        }
    )

    pieces: List[PieceReport] = Field(
        ...,
        description="Liste complète des pièces ou parties du bien incluses dans le rapport de dommages."
    )