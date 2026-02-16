# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SuccessResponse", "Attribution"]


class Attribution(BaseModel):
    """Attribution object to display in user-facing interfaces."""

    text: str
    """Attribution text."""

    url: str
    """Attribution link."""


class SuccessResponse(BaseModel):
    attribution: Attribution
    """Attribution object to display in user-facing interfaces."""

    success: Literal[True]
