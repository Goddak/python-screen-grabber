import ctypes
import os
from PIL import Image
import time

LibName = 'prtscn.so'
AbsLibPath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + LibName
grab = ctypes.CDLL(AbsLibPath)
file_name_prefix = 'goddak'

def grab_screen(x1,y1,x2,y2):
    w, h = x2-x1, y2-y1
    size = w * h
    objlength = size * 3

    grab.getScreen.argtypes = []
    result = (ctypes.c_ubyte*objlength)()

    grab.getScreen(x1,y1, w, h, result)
    return Image.frombuffer('RGB', (w, h), result, 'raw', 'RGB', 0, 1)

i = 0
while True:
  im = grab_screen(0,0,3840,2160)
  im.save(file_name_prefix + str(i) + '.jpg', 'JPEG')
  i = i + 1
  time.sleep(0.5)