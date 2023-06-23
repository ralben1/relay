import RPi.GPIO as GPIO

relay1 = int
relay2 = int

class Light():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(relay1, GPIO.OUT)
        GPIO.setup(relay2, GPIO.OUT)
        GPIO.output(relay1, GPIO.HIGH)
        GPIO.output(relay2, GPIO.HIGH)
    def light1on(self):
        GPIO.output(relay1, GPIO.LOW)
        return "Light 1 on"

    def light1off(self):
        return "Light 1 off"
        GPIO.output(relay1, GPIO.HIGH)

    def light2on(self):
        GPIO.output(relay2, GPIO.LOW)
        return "Light 2 on"

    def light2off(self):
        return "Light 2 off"
        GPIO.output(relay2, GPIO.HIGH)

    def stop(self):
        GPIO.cleanup()
        return True
