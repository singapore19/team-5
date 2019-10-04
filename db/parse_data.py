import csv
from pprint import pprint

with open('./mockdata.csv') as f:
    reader = csv.DictReader(f)

    pprint({"data": [dict(r) for r in reader]})