# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .coordinates import Coordinates
from .score_label import ScoreLabel
from .success_response import SuccessResponse
from .accessibility_features import AccessibilityFeatures

__all__ = ["LocationRetrieveResponse", "LocationRetrieveResponseData"]


class LocationRetrieveResponseData(BaseModel):
    id: str

    address: str

    city: str

    coordinates: Coordinates

    features: AccessibilityFeatures
    """Six accessibility features evaluated for every location.

    Values are true, false, or null (unknown).
    """

    last_updated: datetime
    """ISO 8601 timestamp of last data update."""

    name: str

    region: str
    """Region identifier."""

    score: int

    score_label: ScoreLabel
    """Human-readable score label.

    Excellent (90-100), Good (70-89), Fair (50-69), Limited (0-49).
    """

    state: str
    """Two-letter state abbreviation."""

    verified: bool

    zip: str

    cuisine: Optional[str] = None

    phone: Optional[str] = None
    """Phone number in E.164-like format."""

    website: Optional[str] = None


class LocationRetrieveResponse(SuccessResponse):
    data: LocationRetrieveResponseData
