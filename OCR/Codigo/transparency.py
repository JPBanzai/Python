from win32api import GetSystemMetrics
import win32con
import win32gui
import wx #pip install wxpython

def scale_bitmap(bitmap, width, height):
    image = wx.Bitmap.ConvertToImage(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

app = wx.App()
trans = 0  #alpha value from 0 to 255
# create a window/frame, no parent, -1 is default ID
# change the size of the frame to fit the backgound images
frame1 = wx.Frame(None, -1, "KEA", style=wx.CLIP_CHILDREN | wx.STAY_ON_TOP)
# create the class instance
frame1.ShowFullScreen(True)
# image_file = win32gui.SystemParametersInfo(win32con.SPI_GETDESKWALLPAPER,0,0)
# bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
# bmp1 = scale_bitmap(bmp1,GetSystemMetrics(1)*1.5,GetSystemMetrics(1))
# bitmap1 = wx.StaticBitmap(frame1, -1, bmp1, (-100, 0))
hwnd = frame1.GetHandle()
 
extendedStyleSettings = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, extendedStyleSettings  | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)

frame1.SetTransparent(trans)

def onKeyDown(e):
    global trans
    key = e.GetKeyCode()
    if  key==wx.WXK_UP:
        print(trans)
        trans+=10
        if trans >255:
            trans = 255
    elif key==wx.WXK_DOWN:
        print(trans)
        trans-=10
        if trans < 0:
            trans = 0
    try:
        win32gui.SetLayeredWindowAttributes(hwnd, 0, trans, win32con.LWA_ALPHA)
    except:
        pass

frame1.Bind(wx.EVT_KEY_DOWN, onKeyDown)

app.MainLoop()