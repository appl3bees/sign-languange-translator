#Exceptions.py

class FrameReadError(Exception):
    def __init__(self, errormessage="Could not get frame, camera is either not plugged in or "
                                    "is disabled. Please enable or plugin your camera."):
        self.errormessage = errormessage
        super().__init__(self.errormessage)

