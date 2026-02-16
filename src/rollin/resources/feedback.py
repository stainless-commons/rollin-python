# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import feedback_submit_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.feedback_submit_response import FeedbackSubmitResponse

__all__ = ["FeedbackResource", "AsyncFeedbackResource"]


class FeedbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/rollin-python#accessing-raw-response-data-eg-headers
        """
        return FeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/rollin-python#with_streaming_response
        """
        return FeedbackResourceWithStreamingResponse(self)

    def submit(
        self,
        *,
        feature: Literal[
            "wheelchair_entry", "accessible_restroom", "level_entry", "accessible_parking", "wide_aisles", "elevator"
        ],
        location_id: str,
        value: bool,
        comment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedbackSubmitResponse:
        """Submit accessibility corrections or updates for a location.

        Feedback is reviewed
        and incorporated into scoring through the verification pipeline. Requires
        Developer tier or higher.

        Args:
          feature: Accessibility feature key.

          location_id: Target location ID.

          value: Reported value for the feature.

          comment: Additional context (max 500 characters).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/feedback",
            body=maybe_transform(
                {
                    "feature": feature,
                    "location_id": location_id,
                    "value": value,
                    "comment": comment,
                },
                feedback_submit_params.FeedbackSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackSubmitResponse,
        )


class AsyncFeedbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/rollin-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/rollin-python#with_streaming_response
        """
        return AsyncFeedbackResourceWithStreamingResponse(self)

    async def submit(
        self,
        *,
        feature: Literal[
            "wheelchair_entry", "accessible_restroom", "level_entry", "accessible_parking", "wide_aisles", "elevator"
        ],
        location_id: str,
        value: bool,
        comment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedbackSubmitResponse:
        """Submit accessibility corrections or updates for a location.

        Feedback is reviewed
        and incorporated into scoring through the verification pipeline. Requires
        Developer tier or higher.

        Args:
          feature: Accessibility feature key.

          location_id: Target location ID.

          value: Reported value for the feature.

          comment: Additional context (max 500 characters).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/feedback",
            body=await async_maybe_transform(
                {
                    "feature": feature,
                    "location_id": location_id,
                    "value": value,
                    "comment": comment,
                },
                feedback_submit_params.FeedbackSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackSubmitResponse,
        )


class FeedbackResourceWithRawResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.submit = to_raw_response_wrapper(
            feedback.submit,
        )


class AsyncFeedbackResourceWithRawResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.submit = async_to_raw_response_wrapper(
            feedback.submit,
        )


class FeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.submit = to_streamed_response_wrapper(
            feedback.submit,
        )


class AsyncFeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.submit = async_to_streamed_response_wrapper(
            feedback.submit,
        )
