import json
import datetime
import random

def add_wisdom(wisdom):
    j = read_json()
    time = str(datetime.datetime.now())
    current_wisdom = {'time_added': time, "truth": wisdom}
    j["wisdoms"].append(current_wisdom)
    write_json(json.dumps(j, ensure_ascii=False))

def read_json():
    with open("brainfuck.json", 'r') as f:
        json_data = json.loads(f.read())
    return json_data

def write_json(data):
    with open("brainfuck.json", 'w') as f:
        f.write(data)

def get_random():
    j = read_json()
    bullshit = j["wisdoms"][random.randint(0,len(j["wisdoms"]) - 1)]
    return bullshit
