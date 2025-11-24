from __future__ import annotations

from stac_cano.datasets.general import Dataset

PC_ENDPOINT = "https://planetarycomputer.microsoft.com/api/stac/v1"


class Sentinel2(Dataset):
    def __init__(self) -> None:
        super().__init__(
            alias="sentinel-2-l2a",
            collections=["sentinel-2-l2a"],
            search=PC_ENDPOINT,
            tags=["optical", "multispectral"],
            start="2015-06-23",
            provider="microsoft",
        )


class Sentinel1(Dataset):
    def __init__(self) -> None:
        super().__init__(
            alias="sentinel-1",
            collections=["sentinel-1-rtc", "sentinel-1-grd"],
            search=PC_ENDPOINT,
            tags=["sar", "radar"],
            start="2014-04-03",
            provider="microsoft",
        )


class GOES(Dataset):
    def __init__(self) -> None:
        super().__init__(
            alias="goes-cmi",
            collections=["goes-cmi"],
            search=PC_ENDPOINT,
            tags=["thermal", "weather", "geostationary"],
            start="2016-01-01",  # Approx start for GOES-16
            provider="microsoft",
        )


class ASTER(Dataset):
    def __init__(self) -> None:
        super().__init__(
            alias="aster-l1t",
            collections=["aster-l1t"],
            search=PC_ENDPOINT,
            tags=["thermal", "optical", "multispectral"],
            start="1999-12-18",
            provider="microsoft",
        )


class MODIS(Dataset):
    def __init__(self) -> None:
        super().__init__(
            alias="modis",
            collections=[
                "modis-14A1-061",  # Thermal Anomalies/Fire
                "modis-21A2-061",  # Land Surface Temp
                "modis-09Q1-061",  # Surface Reflectance
                "modis-43A4-061",  # Nadir BRDF-Adjusted Reflectance
                "modis-11A2-061",  # Land Surface Temp (8-day)
                "modis-16A3GF-061",  # Evapotranspiration
                "modis-10A2-061",  # Snow Cover
                "modis-10A1-061",  # Snow Cover (Daily)
            ],
            search=PC_ENDPOINT,
            tags=["thermal", "optical", "multispectral"],
            start="2000-02-24",
            provider="microsoft",
        )
