import win32api , win32con , time

class KeyBD:
    def __init__(self):
        self.VK_CODE = {'l':0x25,
           '1':0x31,
           'u':0x26,
           'r':0x27,
           'd':0x28}
    def press(self, i):
        win32api.keybd_event(self.VK_CODE[i], 0,0,0)
        time.sleep(.1)
        win32api.keybd_event(self.VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
