import json

test_json = {
  "widget": {
    "debug": "on",
    "window": {
      "title": "Sample Konfabulator Widget",
      "name": "main_window",
      "width": 500,
      "height": 500
    },
    "image": {
      "src": "Images/Sun.png",
      "name": "sun1",
      "hOffset": 250,
      "vOffset": 250,
      "alignment": "center"
    },
    "text": {
      "data": "Click Here",
      "size": 36,
      "style": "bold",
      "name": "text1",
      "hOffset": 250,
      "vOffset": 100,
      "alignment": "center",
      "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
  }
}

def reading_JSON_term():
    json_string = json.dumps(test_json)
    Dict = json.loads(json_string)
    print('JSON as Prolog dict:', Dict)
    print('Access field "widget.text.data":', Dict['widget']['text']['data'])
    print('Alter field "widget":', Dict['widget'].update({'Altered'}))

def searalize_a_JSON_term():
    Dict = {
      "book": {
        "title": "To Mock a Mocking Bird",
        "author": {
          "first_name": "Ramond",
          "last_name": "Smullyan"
        },
        "publisher": "Alfred A. Knopf",
        "year": 1985
      }
    }
    print(json.dumps(Dict))

reading_JSON_term()
searalize_a_JSON_term()