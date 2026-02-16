# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FeatureBreakdownEntry"]


class FeatureBreakdownEntry(BaseModel):
    confidence: float
    """Verification confidence (0.0 to 1.0)."""

    impact: Literal["high", "medium", "low"]
    """How much this feature affects the overall score."""

    value: Optional[bool] = None
    """Feature value (true, false, or null for unknown)."""
