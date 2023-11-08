```python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import Data.IORef

main :: IO ()
main = do
  _ <- Gtk.init Nothing

  -- Create a new window
  window <- new Gtk.Window []

  -- Create a new label and button
  label <- new Gtk.Label [ #label := "0" ]
  button <- new Gtk.Button [ #label := "Click me" ]

  -- Create an IORef to keep track of click count
  clickCount <- newIORef 0

  -- Set up the window and its components
  _ <- #add window label
  _ <- #add window button
  _ <- on button #clicked $ do
    modifyIORef clickCount (+1)
    count <- readIORef clickCount
    #setLabel label (show count)

  -- Start the GUI event loop
  _ <- on window #destroy Gtk.mainQuit
  #showAll window
  Gtk.main
```