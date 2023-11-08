import json

class MyJsonObject:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    def getFoo(self):
        return self.foo

    def getBar(self):
        return self.bar

def main():
    json_data = '{ "foo": 1, "bar": [ "10", "apples"] }'
    obj = json.loads(json_data, object_hook=lambda d: MyJsonObject(d['foo'], d['bar']))

    print(obj.getFoo())

    for bar in obj.getBar():
        print(bar)

    obj = MyJsonObject(2, ["20", "oranges"])
    json_data = json.dumps(obj.__dict__)

    print(json_data)

if __name__ == "__main__":
    main()