# Rtv meteor data for db
# sqlite-utils tables russian-ads.db --counts
# sqlite-utils tables russian-ads.db --counts --csv
# sqlite-utils russian-ads.db "select category, count(*) from targets group by category"

import requests
import sqlite_utils

db = sqlite_utils.Database("meteorites.db")
db["meteorites"].insert_all(
    requests.get(
        "https://data.nasa.gov/resource/y77d-th95.json"
    ).json(),
    pk="id"
)