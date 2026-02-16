# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LocationListParams"]


class LocationListParams(TypedDict, total=False):
    lat: Required[float]
    """Latitude of search center"""

    lng: Required[float]
    """Longitude of search center"""

    cuisine: str
    """Filter by cuisine type (e.g. sushi, italian, mexican)."""

    cursor: str
    """Pagination cursor from a previous response."""

    features: str
    """Comma-separated feature requirements (e.g.

    wheelchair_entry,accessible_restroom).
    """

    limit: int
    """Results per page. Default 20. Max 50."""

    min_score: int
    """Minimum accessibility score (0-100). Default 0."""

    radius: float
    """Search radius in miles. Default 5. Max 25."""
