import json
from pprint import pprint

with open('data.json') as f:
    data = json.load(f)['data']

# get the headers in first
headers = data[0].keys()
dont_want = {"longitude", "latitude", }

table = """
<table class='my-table'>
    <tr>
"""

for header in headers:
    if header not in dont_want:
        header = " ".join(header.split('_'))
        table += f"<th>{header.title()}</th>"

table += "</tr>"

# add the data
for item in data:
    pn = item['phone_number']
    g = item['gender']
    age = " ".join(item['age'].split('_')).title()
    time = item['time'].split(' ')[0]
    eth = item['ethnicity']
    notes = item['notes']
    sev = item['severity']
    loc = item['region']

    table += f"""
    <tr>
    <td>{pn}</td>
    <td>{g}</td>
    <td>{age}</td>
    <td>{time}</td>
    <td>{eth}</td>
    <td>{notes}</td>
    <td>{sev}</td>
    <td>{loc}</td>
    </tr>
    """

table += '</table>'

with open('table.txt', 'w') as f:
    f.write(table)
