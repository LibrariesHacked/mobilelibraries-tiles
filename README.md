# Mobile libraries tiles

Vector tiles for the mobile libraries project to be used in web mapping.

## How it works

### Source data

The [Mobile libraries API](https://github.com/LibrariesHacked/mobilelibraries-api) exposes endpoints to retrieve mobile library stops and trips (route lines between stops) as GeoJSON data.

These are available at:

- [https://api.mobilelibraries.org/api/stops](https://api.mobilelibraries.org/api/stops)
- [https://api.mobilelibraries.org/api/trips](https://api.mobilelibraries.org/api/stops)

By default the data is returned as a JSON array, but by passing the 'Accept' header of `application/geo+json` in the request, the data will return as GeoJSON.

### Downloading the data

The two data sources are downloaded using a Python script, `download.py`. This script uses the `requests` library to download the GeoJSON from the API, and saves it to files in the `data` directory: `stops.geojson` and `trips.geojson`.

### Generating the tiles

Tippecanoe is used to convert both the GeoJSON source files to a directory of static tiles within the `tiles` directory (see `generate.sh`)

### Publishing the tiles

This repository is published as a GitHub pages site (in the Github repository settings), which makes the tiles available in high performance web hosting.

A custom domain is then used to make the tiles available under the `tiles.mobilelibraries.org` domain.

## How to use

These vector tiles are made available via GitHub pages and a custom domain.

Use the URL pattern of `https://tiles.mobilelibraries.org/tiles/{z}/{x}/{y}.mvt` in your preferred mapping library.

When adding the tiles to a map you will need to specify the layers you want to display. The layers available are:

- `stops`
- `trips`

## Licence

The tiles are from data compiled by the public and by public library services. They are licensed under the [Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

Code in this repository is available under the [MIT Licence](LICENSE).
