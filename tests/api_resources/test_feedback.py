# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rollin import Rollin, AsyncRollin
from tests.utils import assert_matches_type
from rollin.types import FeedbackSubmitResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit(self, client: Rollin) -> None:
        feedback = client.feedback.submit(
            feature="wheelchair_entry",
            location_id="loc_8f2a9c1b",
            value=True,
        )
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: Rollin) -> None:
        feedback = client.feedback.submit(
            feature="wheelchair_entry",
            location_id="loc_8f2a9c1b",
            value=True,
            comment="Restroom door too narrow for standard wheelchair",
        )
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Rollin) -> None:
        response = client.feedback.with_raw_response.submit(
            feature="wheelchair_entry",
            location_id="loc_8f2a9c1b",
            value=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Rollin) -> None:
        with client.feedback.with_streaming_response.submit(
            feature="wheelchair_entry",
            location_id="loc_8f2a9c1b",
            value=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncRollin) -> None:
        feedback = await async_client.feedback.submit(
            feature="wheelchair_entry",
            location_id="loc_8f2a9c1b",
            value=True,
        )
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncRollin) -> None:
        feedback = await async_client.feedback.submit(
            feature="wheelchair_entry",
            location_id="loc_8f2a9c1b",
            value=True,
            comment="Restroom door too narrow for standard wheelchair",
        )
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncRollin) -> None:
        response = await async_client.feedback.with_raw_response.submit(
            feature="wheelchair_entry",
            location_id="loc_8f2a9c1b",
            value=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncRollin) -> None:
        async with async_client.feedback.with_streaming_response.submit(
            feature="wheelchair_entry",
            location_id="loc_8f2a9c1b",
            value=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True
