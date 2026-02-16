# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .success_response import SuccessResponse

__all__ = ["FeedbackSubmitResponse", "FeedbackSubmitResponseData"]


class FeedbackSubmitResponseData(BaseModel):
    feedback_id: str
    """Unique feedback identifier."""

    message: str

    status: Literal["pending_review"]
    """Current feedback status."""


class FeedbackSubmitResponse(SuccessResponse):
    data: FeedbackSubmitResponseData
