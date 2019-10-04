import random
from datetime import datetime
from pprint import pprint
import csv
import json

def get_random():
    rand_nums = list("12345678")
    eth = ['chinese', 'malay', 'indian', 'others']
    sev = ['Severe', 'Moderate', 'Not urgent']
    regions = ['Changi', 'Jurong West', 'Bukit Panjang', 'Kovan', 'Hougang', 'Sengkang', 'Choa Chu Kang',
    'Pioneer', 'Joo Koon', "Tanjong Pangar", "Bishan", 'Serangoon', 'Pasir Ris', 'Jurong East']

    random.shuffle(rand_nums)
    random.shuffle(rand_nums)
    random.shuffle(rand_nums)

    return {
        "phone_number": int("".join(rand_nums)),
        "gender": random.choice(['male', 'female']),
        "age": get_random_age(),
        "time": str(get_random_time()),
        "ethnicity": random.choice(['chinese', 'malay', 'indian', 'others']),
        "notes": "Testing",
        "severity": random.choice(['Severe', 'Moderate', 'Not urgent']),
        "region": random.choice(regions),
        "longitude": round(get_random_long(), 5),
        "latitude": round(get_random_lat(), 5)
    }

def get_random_age():
    rand_age = random.randint(10, 80)
    age_mapping = {
        10: "children",
        25: "young_adult",
        60: "midlife",
        80: "elderly"
    }

    return random.choice(list(age_mapping.values()))

def get_random_time():
    random_month = random.randint(9, 10)
    random_day = random.randint(1, 30)
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    return datetime(2019, random_month, random_day, random_hour, random_minute, 27, 719598)

def get_random_lat():
    SINGAPORE_LAT = 1.290270
    sg_lat_actual = SINGAPORE_LAT * 10000
    plus_or_minus = random.randint(0, 1)
    rand_num = random.randint(0, 20)
    random_lat = sg_lat_actual + rand_num if plus_or_minus else sg_lat_actual - rand_num

    return random_lat / 10000

def get_random_long():
    SINGAPORE_long = 103.851959
    sg_long_actual = SINGAPORE_long * 1000000
    plus_or_minus = random.randint(0, 1)
    rand_num = random.randint(0, 9000)
    random_long = sg_long_actual + rand_num if plus_or_minus else sg_long_actual - rand_num

    return random_long / 1000000

data = []
for _ in range(100):
    data.append(get_random())

col_names = list(data[0].keys())

with open('mockdata2.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=col_names)
    writer.writeheader()
    writer.writerows(data)

with open('data.json', 'w') as json_f:
    json.dump({"data": data}, json_f, indent=4)