import json

class MyJsonObject:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar
    
    def getFoo(self):
        return self.foo
    
    def getBar(self):
        return self.bar

gson = json
json_str = '{ "foo": 1, "bar": [ "10", "apples"] }'
obj = gson.loads(json_str, object_hook=lambda d: MyJsonObject(**d))

print(obj.getFoo())

for bar in obj.getBar():
    print(bar)

obj = MyJsonObject(2, ["20", "oranges"])
json_str = gson.dumps(obj.__dict__)

print(json_str)