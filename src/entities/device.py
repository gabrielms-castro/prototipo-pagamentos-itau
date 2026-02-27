from src.models import BaseModel


class Device(BaseModel):
    def __init__(self, colorDepth, deviceType3ds, javaEnabled, language, screenHeight, screenWidth, timeZoneOffset):
        self.colorDepth = colorDepth
        self.deviceType3ds = deviceType3ds
        self.javaEnabled = javaEnabled
        self.language = language
        self.screenHeight = screenHeight
        self.screenWidth = screenWidth
        self.timeZoneOffset = timeZoneOffset