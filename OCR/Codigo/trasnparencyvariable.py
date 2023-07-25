from win32api import GetSystemMetrics
import win32con
import win32gui
import wx


app = wx.App()
trans = 0  #alpha value from 0 to 255
# create a window/frame, no parent, -1 is default ID
# change the size of the frame to fit the backgound images
frame1 = wx.Frame(None, -1, "KEA", style=wx.CLIP_CHILDREN | wx.STAY_ON_TOP)
# create the class instance
frame1.ShowFullScreen(True)
hwnd = frame1.GetHandle()

extendedStyleSettings = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, extendedStyleSettings  | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)


# Create a transparent frame
frame = wx.Frame(None, title="Text Display", style=wx.STAY_ON_TOP | wx.CLIP_CHILDREN)
frame.SetPosition((1000,500))

frame.SetSize((200,20))
hwnd = frame.GetHandle()

extendedStyleSettings = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, extendedStyleSettings  | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)

# Create a panel within the frame

frame.SetTransparent(120)
panel = wx.Panel(frame)
panel.SetTransparent(100)
panel.SetSize((200,20))
# Create a static text widget with the desired text
text = wx.StaticText(panel, label="Hello, World!")
text.SetTransparent(255)
text.SetForegroundColour(wx.Colour(255, 0, 0))  # Set text color to red
# Set the font for the text (optional)
font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_EXTRABOLD)
text.SetFont(font)
# Set the text position
text.SetPosition((0, 0))
text.SetSize((200,20))
# Refresh the panel to update the text
panel.Refresh()

frame.Show()

frame1.SetTransparent(trans)

app.MainLoop()