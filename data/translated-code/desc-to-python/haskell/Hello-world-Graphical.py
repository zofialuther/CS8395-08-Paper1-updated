import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def on_dialog_response(dialog, response_id):
    dialog.destroy()

dialog = Gtk.MessageDialog(message_type=Gtk.MessageType.INFO,
                           buttons=Gtk.ButtonsType.OK,
                           text="Goodbye, World!")
dialog.connect("response", on_dialog_response)
dialog.run()