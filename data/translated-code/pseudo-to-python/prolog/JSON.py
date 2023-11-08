import json

def test_json(JSON_string):
    return json.loads(JSON_string)

def reading_JSON_term():
    JSON_string = '{"widget": {"text": {"data": "Hello, World!"}}}'
    Dict = test_json(JSON_string)
    print(Dict)
    print(Dict['widget']['text']['data'])
    Dict['widget'] = "new value"
    print(Dict)

def serialize_a_JSON_term():
    Dict = {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Scribner",
        "year": 1925
    }
    print(json.dumps(Dict))