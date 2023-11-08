```python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def messDialog():
    def on_destroy(widget, data=None):
        Gtk.main_quit()

    def on_response(dialog, response_id, data=None):
        if response_id == Gtk.ResponseType.OK:
            dialog.destroy()

    dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                               Gtk.ButtonsType.OK, "Goodbye, World!")
    dialog.connect("response", on_response)
    dialog.connect("destroy", on_destroy)
    dialog.show_all()

    Gtk.main()
```