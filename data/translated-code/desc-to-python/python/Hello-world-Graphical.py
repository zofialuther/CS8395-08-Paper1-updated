```python
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder

kv_string = '''
FloatLayout:
    Button:
        text: 'Goodbye'
        size_hint: 0.2, 0.1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.open_popup()
'''

class GoodByeApp(App):
    def build(self):
        return Builder.load_string(kv_string)

    def open_popup(self):
        content = Label(text='Goodbye, World!')
        popup = Popup(title='Goodbye, World!', content=content, size_hint=(0.75, 0.75), opacity=0.8)
        popup.open()

if __name__ == '__main__':
    GoodByeApp().run()
```