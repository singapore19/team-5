from app import app
from flask import request, jsonify
import logging

import json

@app.route('/')
def index():
    return '<h1>Haha World!</h1>'

@app.route('/api/allProfiles', method = "GET")
'''
json object should look like this
{
    <id> : {
        "lat": 
        "long":
        "phone_no":
        "gender":
        "age":
        "time":
        "ethinicity":
        "desc":
    }

    <id2> : {
        ...
    }
}
'''
sample_data = {
    "data" : [ 
        {
            "lat": 1.333650,
            "long": 103.766480,
            "phone_no": 98758812,
            "gender": "m",
            "age": "middle age",
            "time": 1570159948,
            "id": 1,
            "desc": "Guy wore blue pants",  
            "urgency_level": "low" # low medium high
        }
    ]
}

@app.route('/app/uploadProfile', method = "POST")
sample_data2 =  {
    "lat": 1.333650,
    "long": 103.766480,
    "phone_no": 98758812,
    "gender": "m",
    "age": "middle age",
    "time": 1570159948,
    "id": 1,
    "desc": "Guy wore blue pants"
}

@app.route('/api/mapData', method = "GET")