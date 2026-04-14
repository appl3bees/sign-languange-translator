#Exceptions.py

class FrameReadError(Exception):
    def __init__(self, errormessage="Could not get frame"):
        self.errormessage = errormessage
        super().__init__(self.errormessage)
        
        
class CameraNotFoundError(Exception):
    def __init__(self, errormessage="Could not locate camera please plug in or turn on your camera"):
        self.errormessage = errormessage
        super().__init__(self.errormessage)

