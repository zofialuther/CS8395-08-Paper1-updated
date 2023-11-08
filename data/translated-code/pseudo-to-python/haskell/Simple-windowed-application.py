import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject

def on_button_clicked(button, label):
    v = m.get()
    m.set(v+1)
    label.set_label("There have been " + str(v+1) + " clicks")

def on_window_destroy(window):
    Gtk.main_quit()

def main():
    window = Gtk.Window()
    window.connect("destroy", on_window_destroy)
    window.set_title("Simple Windowed App")
    window.set_border_width(10)

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)

    window.add(hbox)

    label = Gtk.Label("There have been no clicks yet")
    button = Gtk.Button(label="Click me")
    button.connect("clicked", on_button_clicked, label)

    hbox.pack_start(label, True, True, 0)
    hbox.pack_start(button, True, True, 0)

    m = GObject.Value(0)

    window.show_all()

    Gtk.main()

if __name__ == "__main__":
    main()