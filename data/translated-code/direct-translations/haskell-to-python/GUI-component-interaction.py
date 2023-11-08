import wx
import random

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Interact")

text_entry = wx.TextCtrl(frame, wx.ID_ANY, "0")
increment_button = wx.Button(frame, wx.ID_ANY, "increment")
random_button = wx.Button(frame, wx.ID_ANY, "random")

sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(text_entry, 0, wx.ALIGN_CENTER | wx.ALL, 5)
sizer.Add(increment_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)
sizer.Add(random_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

frame.SetSizer(sizer)
frame.Layout()

def on_increment(event):
    val = int(text_entry.GetValue())
    text_entry.SetValue(str(val + 1))

def on_random(event):
    generate_random_number()

def generate_random_number():
    answer = wx.MessageBox("Generate a random number?", "Random", wx.YES_NO | wx.ICON_QUESTION)
    if answer == wx.YES:
        num = random.randint(1, 100)
        text_entry.SetValue(str(num))

increment_button.Bind(wx.EVT_BUTTON, on_increment)
random_button.Bind(wx.EVT_BUTTON, on_random)

frame.Show(True)
app.MainLoop()