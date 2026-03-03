# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import RollinError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import score, regions, feedback, locations
    from .resources.score import ScoreResource, AsyncScoreResource
    from .resources.regions import RegionsResource, AsyncRegionsResource
    from .resources.feedback import FeedbackResource, AsyncFeedbackResource
    from .resources.locations import LocationsResource, AsyncLocationsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Rollin", "AsyncRollin", "Client", "AsyncClient"]


class Rollin(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Rollin client instance.

        This automatically infers the `api_key` argument from the `ROLLIN_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ROLLIN_API_KEY")
        if api_key is None:
            raise RollinError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ROLLIN_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ROLLIN_BASE_URL")
        if base_url is None:
            base_url = f"https://joinrollin.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def locations(self) -> LocationsResource:
        from .resources.locations import LocationsResource

        return LocationsResource(self)

    @cached_property
    def regions(self) -> RegionsResource:
        from .resources.regions import RegionsResource

        return RegionsResource(self)

    @cached_property
    def feedback(self) -> FeedbackResource:
        from .resources.feedback import FeedbackResource

        return FeedbackResource(self)

    @cached_property
    def score(self) -> ScoreResource:
        from .resources.score import ScoreResource

        return ScoreResource(self)

    @cached_property
    def with_raw_response(self) -> RollinWithRawResponse:
        return RollinWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RollinWithStreamedResponse:
        return RollinWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key_header if security.get("api_key_header", False) else {}),
        }

    @property
    def _api_key_header(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-Api-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncRollin(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncRollin client instance.

        This automatically infers the `api_key` argument from the `ROLLIN_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ROLLIN_API_KEY")
        if api_key is None:
            raise RollinError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ROLLIN_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ROLLIN_BASE_URL")
        if base_url is None:
            base_url = f"https://joinrollin.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResource:
        from .resources.locations import AsyncLocationsResource

        return AsyncLocationsResource(self)

    @cached_property
    def regions(self) -> AsyncRegionsResource:
        from .resources.regions import AsyncRegionsResource

        return AsyncRegionsResource(self)

    @cached_property
    def feedback(self) -> AsyncFeedbackResource:
        from .resources.feedback import AsyncFeedbackResource

        return AsyncFeedbackResource(self)

    @cached_property
    def score(self) -> AsyncScoreResource:
        from .resources.score import AsyncScoreResource

        return AsyncScoreResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncRollinWithRawResponse:
        return AsyncRollinWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRollinWithStreamedResponse:
        return AsyncRollinWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key_header if security.get("api_key_header", False) else {}),
        }

    @property
    def _api_key_header(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-Api-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class RollinWithRawResponse:
    _client: Rollin

    def __init__(self, client: Rollin) -> None:
        self._client = client

    @cached_property
    def locations(self) -> locations.LocationsResourceWithRawResponse:
        from .resources.locations import LocationsResourceWithRawResponse

        return LocationsResourceWithRawResponse(self._client.locations)

    @cached_property
    def regions(self) -> regions.RegionsResourceWithRawResponse:
        from .resources.regions import RegionsResourceWithRawResponse

        return RegionsResourceWithRawResponse(self._client.regions)

    @cached_property
    def feedback(self) -> feedback.FeedbackResourceWithRawResponse:
        from .resources.feedback import FeedbackResourceWithRawResponse

        return FeedbackResourceWithRawResponse(self._client.feedback)

    @cached_property
    def score(self) -> score.ScoreResourceWithRawResponse:
        from .resources.score import ScoreResourceWithRawResponse

        return ScoreResourceWithRawResponse(self._client.score)


class AsyncRollinWithRawResponse:
    _client: AsyncRollin

    def __init__(self, client: AsyncRollin) -> None:
        self._client = client

    @cached_property
    def locations(self) -> locations.AsyncLocationsResourceWithRawResponse:
        from .resources.locations import AsyncLocationsResourceWithRawResponse

        return AsyncLocationsResourceWithRawResponse(self._client.locations)

    @cached_property
    def regions(self) -> regions.AsyncRegionsResourceWithRawResponse:
        from .resources.regions import AsyncRegionsResourceWithRawResponse

        return AsyncRegionsResourceWithRawResponse(self._client.regions)

    @cached_property
    def feedback(self) -> feedback.AsyncFeedbackResourceWithRawResponse:
        from .resources.feedback import AsyncFeedbackResourceWithRawResponse

        return AsyncFeedbackResourceWithRawResponse(self._client.feedback)

    @cached_property
    def score(self) -> score.AsyncScoreResourceWithRawResponse:
        from .resources.score import AsyncScoreResourceWithRawResponse

        return AsyncScoreResourceWithRawResponse(self._client.score)


class RollinWithStreamedResponse:
    _client: Rollin

    def __init__(self, client: Rollin) -> None:
        self._client = client

    @cached_property
    def locations(self) -> locations.LocationsResourceWithStreamingResponse:
        from .resources.locations import LocationsResourceWithStreamingResponse

        return LocationsResourceWithStreamingResponse(self._client.locations)

    @cached_property
    def regions(self) -> regions.RegionsResourceWithStreamingResponse:
        from .resources.regions import RegionsResourceWithStreamingResponse

        return RegionsResourceWithStreamingResponse(self._client.regions)

    @cached_property
    def feedback(self) -> feedback.FeedbackResourceWithStreamingResponse:
        from .resources.feedback import FeedbackResourceWithStreamingResponse

        return FeedbackResourceWithStreamingResponse(self._client.feedback)

    @cached_property
    def score(self) -> score.ScoreResourceWithStreamingResponse:
        from .resources.score import ScoreResourceWithStreamingResponse

        return ScoreResourceWithStreamingResponse(self._client.score)


class AsyncRollinWithStreamedResponse:
    _client: AsyncRollin

    def __init__(self, client: AsyncRollin) -> None:
        self._client = client

    @cached_property
    def locations(self) -> locations.AsyncLocationsResourceWithStreamingResponse:
        from .resources.locations import AsyncLocationsResourceWithStreamingResponse

        return AsyncLocationsResourceWithStreamingResponse(self._client.locations)

    @cached_property
    def regions(self) -> regions.AsyncRegionsResourceWithStreamingResponse:
        from .resources.regions import AsyncRegionsResourceWithStreamingResponse

        return AsyncRegionsResourceWithStreamingResponse(self._client.regions)

    @cached_property
    def feedback(self) -> feedback.AsyncFeedbackResourceWithStreamingResponse:
        from .resources.feedback import AsyncFeedbackResourceWithStreamingResponse

        return AsyncFeedbackResourceWithStreamingResponse(self._client.feedback)

    @cached_property
    def score(self) -> score.AsyncScoreResourceWithStreamingResponse:
        from .resources.score import AsyncScoreResourceWithStreamingResponse

        return AsyncScoreResourceWithStreamingResponse(self._client.score)


Client = Rollin

AsyncClient = AsyncRollin
