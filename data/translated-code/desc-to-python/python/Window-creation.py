import win32ui
import pywin.mfc.dialog

class SimpleInputDialog(pywin.mfc.dialog.Dialog):
    def __init__(self):
        pywin.mfc.dialog.Dialog.__init__(self, win32ui.IDD_SIMPLE_INPUT)

    def DoDataExchange(self, dx):
        self.exchange = pywin.mfc.dialog.Exchange(dx)
        self.exchange.DDX_Text(win32ui.IDC_EDIT1, self.input_text)

    def OnInitDialog(self):
        self.input_text = ""
        return 1

# Create window
dlg = SimpleInputDialog()
dlg.CreateWindow()