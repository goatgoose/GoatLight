import RPi.GPIO as GPIO


class GoatLight:
    def __init__(self):
        self.CONDITIONER_GPIO_NUMBER = 27

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.CONDITIONER_GPIO_NUMBER, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.CONDITIONER_GPIO_NUMBER, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.CONDITIONER_GPIO_NUMBER, GPIO.LOW)
