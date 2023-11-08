import json
import Data.Aeson as A

testdoc = {
    "key1": "value1",
    "key2": "value2"
}

def main():
    out = A.encode(testdoc)
    print(out)
    v = A.parseOnly(out)
    if v.isLeft():
        error = "strange error re-parsing json: " + v.value0
        raise ValueError(error)
    elif v.value0 != testdoc:
        raise ValueError("documents not equal!")
    else:
        print(v.value0)