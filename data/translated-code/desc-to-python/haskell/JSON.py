```python
import json

# create a JSON object with various data types
data = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "grades": [90, 85, 88],
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    }
}

# encode the JSON object into a bytestring
json_string = json.dumps(data)

# parse the bytestring back into JSON
parsed_json = json.loads(json_string)

# compare the parsed JSON with the original object
if parsed_json != data:
    print("Error: Parsed JSON is not equal to original object")
else:
    print(parsed_json)
```