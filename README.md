# Mobile libraries tiles

Vector tiles for the mobile libraries project

## How it works

The [Mobile libraries API](https://github.com/LibrariesHacked/mobilelibraries-api) exposes endpoints to retrieve mobile library stops and trips as GeoJSON. This repository contains scripts that will extract these GeoJSON files on a nightly basis and convert them into static vector tiles.

Those vector tiles are then available as [Mapbox Vector Tiles](https://github.com/mapbox/vector-tile-spec) for use in web maps. There will be two layers embedded into each tile: `stops` and `trips`. The `stops` layer contains the location of each stop, and the `trips` layer contains the route taken by the mobile library between different stops.

The process is as follows:

1. Download the latest GeoJSON from the Mobile libraries API (see `download.py`).
2. Use tippecanoe to convert the GeoJSON to a directory of static tiles within the `\libraries` directory (see `generate.sh`)

This repository is published as a GitHub pages site, which makes the tiles available in high performance web hosting.

## How to use

These tiles are made available via GitHub pages and a custom domain. They are available at `https://tiles.mobilelibraries.org/tiles/{z}/{x}/{y}.mvt`

## Licence

The tiles are from data compiled by the public and by public library services. They are licensed under the [Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

Code in this repository is available under the [MIT Licence](LICENSE).
