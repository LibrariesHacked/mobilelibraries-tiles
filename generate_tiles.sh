mkdir tiles
tippecanoe -r1 --no-tile-compression --drop-densest-as-needed --no-tile-size-limit --output-to-directory tiles data/trips.geojson data/stops.geojson  --force
find . -name '*.pbf' -exec sh -c 'mv "$0" "${0%.pbf}.mvt"' {} \;
