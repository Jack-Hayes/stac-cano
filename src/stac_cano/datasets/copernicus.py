from __future__ import annotations

from stac_cano.datasets.general import Dataset

COPERNICUS_ENDPOINT = "https://stac.dataspace.copernicus.eu/v1"


class Sentinel3(Dataset):
    def __init__(self) -> None:
        super().__init__(
            alias="sentinel-3",
            collections=[
                "sentinel-3-sl-2-lst-ntc",  # Land Surface Temp
                "sentinel-3-syn-2-syn-ntc",  # Synergy
                "sentinel-3-olci-1-efr-ntc",  # Ocean Land Color
            ],
            search=COPERNICUS_ENDPOINT,
            tags=["thermal", "optical", "multispectral"],
            start="2016-02-16",
            provider="copernicus",
        )
