# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccessibilityFeatures"]


class AccessibilityFeatures(BaseModel):
    """Six accessibility features evaluated for every location.

    Values are true, false, or null (unknown).
    """

    accessible_parking: Optional[bool] = None
    """Standard feature: accessible parking available."""

    accessible_restroom: Optional[bool] = None
    """Critical feature: wheelchair-accessible restroom."""

    elevator: Optional[bool] = None
    """Standard feature: elevator access."""

    level_entry: Optional[bool] = None
    """Critical feature: level (no-step) entry."""

    wheelchair_entry: Optional[bool] = None
    """Critical feature: wheelchair-accessible entrance."""

    wide_aisles: Optional[bool] = None
    """Standard feature: wide aisles for wheelchair navigation."""
