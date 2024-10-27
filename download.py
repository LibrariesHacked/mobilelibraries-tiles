""" Download the geojson files from the Mobile libraries API and save to data directory. """

import json
import os
import requests

GEOJSON_STOPS_URL = 'https://api.mobilelibraries.org/api/stops?limit=20000'
GEOJSON_TRIPS_URL = 'https://api.mobilelibraries.org/api/trips'


def download_geojson(url):
    """Download the geojson file and return the json data."""

    headers = {"Accept": "application/geo+json"}
    response = requests.get(url, headers=headers, timeout=10)
    return response.json()


def save_geojson(data, file_name):
    """Save the geojson data to the data directory."""

    if not os.path.exists('data'):
        os.makedirs('data')

    with open(f'data/{file_name}', 'w', encoding='utf-8') as f:
        json.dump(data, f)


stops_geojson = download_geojson(GEOJSON_STOPS_URL)
save_geojson(stops_geojson, 'stops.geojson')

trips_geojson = download_geojson(GEOJSON_TRIPS_URL)
save_geojson(trips_geojson, 'trips.geojson')
