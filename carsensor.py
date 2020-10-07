from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24
print("check 1")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print("check 2")
time.sleep(1)

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            start = time.time()
        while GPIO_input(ECHO) == 1:
            stop = time.time()

         check_time = stop - start
         distance = check_time * 34300/2
         print("Distance : %.1f cm" % distance)
         time.sleep(0.1)   

pins = {
    12 : {'name':'RED', 'state':GPIO.LOW }
    }

for pin in pins:
    GPIO.setup(pin , GPIO.OUT)
    GPIO.output(pin , GPIO.LOW)
    
@app.route("/")
def main():
    for pin in pins:
       pins[pin]['state'] = GPIO.input(pin)
    temp = {
        'pins' : pins
        }
    return render_template('app.html', **temp)

@app.route("/<changePin>/<action>")
def action(changePin, action):
    pin = int(changePin)
    
    if action == 'on':
        GPIO.output(pin, GPIO.HIGH)
    if action == 'off':
        GPIO.output(pin, GPIO.LOW)
    
    for pin in pins:
       pins[pin]['state'] = GPIO.input(pin)
    temp = {
        'pins' : pins
        }      
    return render_template('app.html', **temp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000, debug=True)