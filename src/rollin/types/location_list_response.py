# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .score_label import ScoreLabel

__all__ = ["LocationListResponse"]


class LocationListResponse(BaseModel):
    id: str
    """Unique location identifier."""

    address: str
    """Full street address."""

    category: str
    """Location category."""

    distance_miles: float
    """Distance from search center in miles."""

    lat: float
    """Latitude."""

    lng: float
    """Longitude."""

    name: str
    """Location name."""

    score: int
    """Accessibility score (0-100)."""

    score_label: ScoreLabel
    """Human-readable score label.

    Excellent (90-100), Good (70-89), Fair (50-69), Limited (0-49).
    """
