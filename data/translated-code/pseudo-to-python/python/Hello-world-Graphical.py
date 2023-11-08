```python
# Import the necessary libraries
from kivy.app import App
from kivy.lang import Builder

# Define the kv string with the Kivy language code for the layout and popup
kv = '''
BoxLayout:
    Button:
        text: 'Goodbye!'
'''

# Create a class GoodByeApp that inherits from App
class GoodByeApp(App):
    # Define the build method in GoodByeApp class
    def build(self):
        # Load the layout and popup from the kv string using Builder.load_string
        return Builder.load_string(kv)

# Instantiate the GoodByeApp and run it
if __name__ == '__main__':
    GoodByeApp().run()
```