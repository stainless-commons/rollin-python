# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import location_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPagination, AsyncCursorPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.location_list_response import LocationListResponse
from ..types.location_retrieve_response import LocationRetrieveResponse

__all__ = ["LocationsResource", "AsyncLocationsResource"]


class LocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-commons/rollin-python#accessing-raw-response-data-eg-headers
        """
        return LocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-commons/rollin-python#with_streaming_response
        """
        return LocationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationRetrieveResponse:
        """
        Get full detail for a single location, including all accessibility features,
        score, and metadata. Requires Developer tier or higher.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/locations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationRetrieveResponse,
        )

    def list(
        self,
        *,
        lat: float,
        lng: float,
        cuisine: str | Omit = omit,
        cursor: str | Omit = omit,
        features: str | Omit = omit,
        limit: int | Omit = omit,
        min_score: int | Omit = omit,
        radius: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[LocationListResponse]:
        """Search wheelchair-accessible locations by geographic area.

        Returns scored,
        verified results sorted by relevance. Requires Developer tier or higher.

        Args:
          lat: Latitude of search center

          lng: Longitude of search center

          cuisine: Filter by cuisine type (e.g. sushi, italian, mexican).

          cursor: Pagination cursor from a previous response.

          features: Comma-separated feature requirements (e.g.
              wheelchair_entry,accessible_restroom).

          limit: Results per page. Default 20. Max 50.

          min_score: Minimum accessibility score (0-100). Default 0.

          radius: Search radius in miles. Default 5. Max 25.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/locations",
            page=SyncCursorPagination[LocationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "cuisine": cuisine,
                        "cursor": cursor,
                        "features": features,
                        "limit": limit,
                        "min_score": min_score,
                        "radius": radius,
                    },
                    location_list_params.LocationListParams,
                ),
            ),
            model=LocationListResponse,
        )


class AsyncLocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-commons/rollin-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-commons/rollin-python#with_streaming_response
        """
        return AsyncLocationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationRetrieveResponse:
        """
        Get full detail for a single location, including all accessibility features,
        score, and metadata. Requires Developer tier or higher.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/locations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationRetrieveResponse,
        )

    def list(
        self,
        *,
        lat: float,
        lng: float,
        cuisine: str | Omit = omit,
        cursor: str | Omit = omit,
        features: str | Omit = omit,
        limit: int | Omit = omit,
        min_score: int | Omit = omit,
        radius: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LocationListResponse, AsyncCursorPagination[LocationListResponse]]:
        """Search wheelchair-accessible locations by geographic area.

        Returns scored,
        verified results sorted by relevance. Requires Developer tier or higher.

        Args:
          lat: Latitude of search center

          lng: Longitude of search center

          cuisine: Filter by cuisine type (e.g. sushi, italian, mexican).

          cursor: Pagination cursor from a previous response.

          features: Comma-separated feature requirements (e.g.
              wheelchair_entry,accessible_restroom).

          limit: Results per page. Default 20. Max 50.

          min_score: Minimum accessibility score (0-100). Default 0.

          radius: Search radius in miles. Default 5. Max 25.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/locations",
            page=AsyncCursorPagination[LocationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "cuisine": cuisine,
                        "cursor": cursor,
                        "features": features,
                        "limit": limit,
                        "min_score": min_score,
                        "radius": radius,
                    },
                    location_list_params.LocationListParams,
                ),
            ),
            model=LocationListResponse,
        )


class LocationsResourceWithRawResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.retrieve = to_raw_response_wrapper(
            locations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            locations.list,
        )


class AsyncLocationsResourceWithRawResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.retrieve = async_to_raw_response_wrapper(
            locations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            locations.list,
        )


class LocationsResourceWithStreamingResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.retrieve = to_streamed_response_wrapper(
            locations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            locations.list,
        )


class AsyncLocationsResourceWithStreamingResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.retrieve = async_to_streamed_response_wrapper(
            locations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            locations.list,
        )
