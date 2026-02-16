# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Coordinates"]


class Coordinates(BaseModel):
    lat: float
    """Latitude."""

    lng: float
    """Longitude."""
