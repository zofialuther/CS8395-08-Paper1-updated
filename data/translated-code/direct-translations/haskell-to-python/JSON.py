```python
import json
import sys

testdoc = {
    "foo": 1,
    "bar": [1.3, 1.6, 1.9],
    "baz": "some string",
    "other": {
        "yes": "sir"
    }
}

out = json.dumps(testdoc, indent=4)
print(out)

try:
    parsed_doc = json.loads(out)
    if parsed_doc != testdoc:
        raise ValueError("documents not equal!")
    print(parsed_doc)
except json.JSONDecodeError as e:
    print(f"Error re-parsing json: {e}")
    sys.exit(1)
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)
```