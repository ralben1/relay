import RPi.GPIO as GPIO

relay1 = int
relay2 = int

class Light():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(relay1, GPIO.OUT)
        GPIO.setup(relay2, GPIO.OUT)
    def light1on(self):
        return "Light 1 on"

    def light1off(self):
        return "Light 1 off"

    def light2on(self):
        return "Light 2 on"

    def light2off(self):
        return "Light 2 off"
