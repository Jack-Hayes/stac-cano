from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Dataset:
    """
    Essential metadata for supported datasets.

    Attributes:
        alias: Unique nickname for the dataset (e.g., 's2-l2a').
        collections: List of STAC collection IDs associated with this dataset.
        search: The STAC API endpoint URL.
        tags: Descriptive tags for filtering (e.g., 'optical', 'sar', 'thermal').
        start: Start date of the dataset (ISO 8601).
        end: End date of the dataset (ISO 8601) or None if ongoing.
        provider: Name of the data provider (e.g., 'microsoft', 'usgs').
        stac_kwargs: Additional keyword arguments for the pystac client search.
    """

    alias: str
    collections: list[str]
    search: str
    tags: list[str]
    start: str
    end: str | None = None
    provider: str | None = None
    stac_kwargs: dict[str, Any] = field(default_factory=lambda: {"limit": 500})
