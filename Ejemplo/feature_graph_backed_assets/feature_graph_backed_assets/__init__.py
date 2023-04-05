from dagster import (
    AssetsDefinition,
    AssetSelection,
    Definitions,
    define_asset_job,
    load_assets_from_package_module,
)

from . import assets
from .graphs_and_ops import layover_breakdown_2022, us_assets

airline_job = define_asset_job("airline_job", AssetSelection.keys("passenger_flights").downstream())


defs = Definitions(
    assets=[
        *load_assets_from_package_module(assets),
        AssetsDefinition.from_graph(us_assets),
        AssetsDefinition.from_graph(layover_breakdown_2022),
    ],
    jobs=[define_asset_job("airline_job", AssetSelection.keys("passenger_flights").downstream())],
)
