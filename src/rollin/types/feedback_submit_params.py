# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FeedbackSubmitParams"]


class FeedbackSubmitParams(TypedDict, total=False):
    feature: Required[
        Literal[
            "wheelchair_entry", "accessible_restroom", "level_entry", "accessible_parking", "wide_aisles", "elevator"
        ]
    ]
    """Accessibility feature key."""

    location_id: Required[str]
    """Target location ID."""

    value: Required[bool]
    """Reported value for the feature."""

    comment: str
    """Additional context (max 500 characters)."""
