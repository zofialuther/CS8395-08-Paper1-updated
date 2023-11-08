```python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def messDialog():
    Gtk.init()
    dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Goodbye, World!")

    rs = dialog.run()
    if rs == Gtk.ResponseType.OK or rs == Gtk.ResponseType.DELETE_EVENT:
        dialog.destroy()

    dialog.connect("destroy", Gtk.main_quit)

    Gtk.main()

messDialog()
```