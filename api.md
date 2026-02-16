# Locations

Types:

```python
from rollin.types import (
    AccessibilityFeatures,
    Coordinates,
    ScoreLabel,
    SuccessResponse,
    LocationRetrieveResponse,
    LocationListResponse,
)
```

Methods:

- <code title="get /locations/{id}">client.locations.<a href="./src/rollin/resources/locations.py">retrieve</a>(id) -> <a href="./src/rollin/types/location_retrieve_response.py">LocationRetrieveResponse</a></code>
- <code title="get /locations">client.locations.<a href="./src/rollin/resources/locations.py">list</a>(\*\*<a href="src/rollin/types/location_list_params.py">params</a>) -> <a href="./src/rollin/types/location_list_response.py">SyncCursorPagination[LocationListResponse]</a></code>

# Regions

Types:

```python
from rollin.types import RegionListResponse
```

Methods:

- <code title="get /regions">client.regions.<a href="./src/rollin/resources/regions.py">list</a>() -> <a href="./src/rollin/types/region_list_response.py">RegionListResponse</a></code>

# Feedback

Types:

```python
from rollin.types import FeedbackSubmitResponse
```

Methods:

- <code title="post /feedback">client.feedback.<a href="./src/rollin/resources/feedback.py">submit</a>(\*\*<a href="src/rollin/types/feedback_submit_params.py">params</a>) -> <a href="./src/rollin/types/feedback_submit_response.py">FeedbackSubmitResponse</a></code>

# Score

Types:

```python
from rollin.types import FeatureBreakdownEntry, ScoreRetrieveResponse
```

Methods:

- <code title="get /score/{id}">client.score.<a href="./src/rollin/resources/score.py">retrieve</a>(id) -> <a href="./src/rollin/types/score_retrieve_response.py">ScoreRetrieveResponse</a></code>
