from __future__ import annotations

from stac_cano.datasets.general import Dataset

USGS_ENDPOINT = "https://landsatlook.usgs.gov/stac-server"


class Landsat(Dataset):
    def __init__(self) -> None:
        super().__init__(
            alias="landsat",
            collections=["landsat-c2l2-sr", "landsat-c2l2-st"],
            search=USGS_ENDPOINT,
            tags=["optical", "thermal", "multispectral"],
            start="1984-01-01",  # Landsat 4/5 era
            provider="usgs",
        )
