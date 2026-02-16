# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .coordinates import Coordinates
from .success_response import SuccessResponse

__all__ = ["RegionListResponse", "RegionListResponseData", "RegionListResponseMeta"]


class RegionListResponseData(BaseModel):
    id: str
    """Region identifier."""

    center: Coordinates

    location_count: int
    """Number of locations in this region."""

    name: str
    """Human-readable region name."""

    state: str
    """Two-letter state abbreviation."""


class RegionListResponseMeta(BaseModel):
    total_locations: int
    """Total locations across all regions."""

    total_regions: int
    """Total number of coverage regions."""


class RegionListResponse(SuccessResponse):
    data: List[RegionListResponseData]

    meta: RegionListResponseMeta
