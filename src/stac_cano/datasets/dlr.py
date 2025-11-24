from __future__ import annotations

from stac_cano.datasets.general import Dataset

DLR_ENDPOINT = "https://geoservice.dlr.de/eoc/ogc/stac/v1"


class TSX(Dataset):
    def __init__(self) -> None:
        super().__init__(
            alias="tsx-supersites",
            collections=["SUPERSITES"],
            search=DLR_ENDPOINT,
            tags=["sar", "radar"],
            start="2007-06-15",
            provider="dlr",
        )
