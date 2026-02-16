# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .score_label import ScoreLabel
from .success_response import SuccessResponse
from .feature_breakdown_entry import FeatureBreakdownEntry

__all__ = ["ScoreRetrieveResponse", "ScoreRetrieveResponseData", "ScoreRetrieveResponseDataBreakdown"]


class ScoreRetrieveResponseDataBreakdown(BaseModel):
    accessible_parking: FeatureBreakdownEntry

    accessible_restroom: FeatureBreakdownEntry

    elevator: FeatureBreakdownEntry

    level_entry: FeatureBreakdownEntry

    wheelchair_entry: FeatureBreakdownEntry

    wide_aisles: FeatureBreakdownEntry


class ScoreRetrieveResponseData(BaseModel):
    breakdown: ScoreRetrieveResponseDataBreakdown

    last_verified: datetime
    """ISO 8601 timestamp of last verification."""

    location_id: str

    score: int

    score_label: ScoreLabel
    """Human-readable score label.

    Excellent (90-100), Good (70-89), Fair (50-69), Limited (0-49).
    """

    verification_count: int
    """Number of community verifications for this location."""


class ScoreRetrieveResponse(SuccessResponse):
    data: ScoreRetrieveResponseData
