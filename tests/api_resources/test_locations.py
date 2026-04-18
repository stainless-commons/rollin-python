# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rollin import Rollin, AsyncRollin
from tests.utils import assert_matches_type
from rollin.types import LocationListResponse, LocationRetrieveResponse
from rollin.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Rollin) -> None:
        location = client.locations.retrieve(
            "id",
        )
        assert_matches_type(LocationRetrieveResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Rollin) -> None:
        response = client.locations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationRetrieveResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Rollin) -> None:
        with client.locations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationRetrieveResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Rollin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.locations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Rollin) -> None:
        location = client.locations.list(
            lat=-90,
            lng=-180,
        )
        assert_matches_type(SyncCursorPagination[LocationListResponse], location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Rollin) -> None:
        location = client.locations.list(
            lat=-90,
            lng=-180,
            cuisine="cuisine",
            cursor="cursor",
            features="features",
            limit=1,
            min_score=0,
            radius=25,
        )
        assert_matches_type(SyncCursorPagination[LocationListResponse], location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Rollin) -> None:
        response = client.locations.with_raw_response.list(
            lat=-90,
            lng=-180,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(SyncCursorPagination[LocationListResponse], location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Rollin) -> None:
        with client.locations.with_streaming_response.list(
            lat=-90,
            lng=-180,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(SyncCursorPagination[LocationListResponse], location, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLocations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRollin) -> None:
        location = await async_client.locations.retrieve(
            "id",
        )
        assert_matches_type(LocationRetrieveResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRollin) -> None:
        response = await async_client.locations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationRetrieveResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRollin) -> None:
        async with async_client.locations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationRetrieveResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRollin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.locations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRollin) -> None:
        location = await async_client.locations.list(
            lat=-90,
            lng=-180,
        )
        assert_matches_type(AsyncCursorPagination[LocationListResponse], location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRollin) -> None:
        location = await async_client.locations.list(
            lat=-90,
            lng=-180,
            cuisine="cuisine",
            cursor="cursor",
            features="features",
            limit=1,
            min_score=0,
            radius=25,
        )
        assert_matches_type(AsyncCursorPagination[LocationListResponse], location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRollin) -> None:
        response = await async_client.locations.with_raw_response.list(
            lat=-90,
            lng=-180,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(AsyncCursorPagination[LocationListResponse], location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRollin) -> None:
        async with async_client.locations.with_streaming_response.list(
            lat=-90,
            lng=-180,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(AsyncCursorPagination[LocationListResponse], location, path=["response"])

        assert cast(Any, response.is_closed) is True
