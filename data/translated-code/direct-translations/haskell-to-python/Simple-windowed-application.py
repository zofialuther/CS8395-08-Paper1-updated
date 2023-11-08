```python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

def on_button_clicked(button, label, counter):
    counter[0] += 1
    label.set_label("There have been " + str(counter[0]) + " clicks")

def main():
    window = Gtk.Window()
    window.connect("destroy", Gtk.main_quit)
    window.set_title("Simple Windowed App")
    window.set_border_width(10)

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)

    window.add(hbox)

    label = Gtk.Label(label="There have been no clicks yet")
    button = Gtk.Button(label="Click me")
    button.connect("clicked", on_button_clicked, label, [0])

    hbox.pack_start(label, True, True, 0)
    hbox.pack_start(button, True, True, 0)

    window.show_all()

    Gtk.main()

if __name__ == "__main__":
    main()
```