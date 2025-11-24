from __future__ import annotations

from stac_cano.datasets import copernicus, dlr, microsoft, usgs
from stac_cano.datasets.general import Dataset

# Registry of supported datasets
_datasets = [
    microsoft.Sentinel2(),
    microsoft.Sentinel1(),
    microsoft.GOES(),
    microsoft.ASTER(),
    microsoft.MODIS(),
    copernicus.Sentinel3(),
    usgs.Landsat(),
    dlr.TSX(),
]

# Create lookup dictionaries
aliases = [x.alias for x in _datasets]
_alias_to_dataset = dict(zip(aliases, _datasets, strict=False))


def get_dataset(alias: str) -> Dataset:
    """Retrieve a Dataset object by its alias."""
    if alias not in _alias_to_dataset:
        msg = f"Dataset alias '{alias}' not found. Available: {aliases}"
        raise ValueError(msg)
    return _alias_to_dataset[alias]


__all__ = [
    "Dataset",
    "copernicus",
    "dlr",
    "microsoft",
    "usgs",
    "get_dataset",
]
