import RPi.GPIO as GPIO


class GoatLight:
    def __init__(self):
        self.CONDITIONER_GPIO_NUMBER = 27

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.CONDITIONER_GPIO_NUMBER, GPIO.OUT)

        self.is_on = False

    def turn_on(self):
        GPIO.output(self.CONDITIONER_GPIO_NUMBER, GPIO.HIGH)
        self.is_on = True

    def turn_off(self):
        GPIO.output(self.CONDITIONER_GPIO_NUMBER, GPIO.LOW)
        self.is_on = False
