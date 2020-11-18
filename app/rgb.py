import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # choose BCM numbering scheme.   
GPIO.setup(17, GPIO.OUT)# set GPIO 17 as output for white led  
GPIO.setup(27, GPIO.OUT)# set GPIO 27 as output for red led  
GPIO.setup(22, GPIO.OUT)# set GPIO 22 as output for red led

red = GPIO.PWM(17, 75)    # create object red for PWM on port 17  
green = GPIO.PWM(27, 75)      # create object green for PWM on port 27   
blue = GPIO.PWM(22, 75)      # create object blue for PWM on port 22 
red.start((125/2.55))   #start red led
green.start((125/2.55)) #start green led
blue.start((125/2.55))

def RGBColor(redc, greenc, bluec):
    red.start((redc/2.55))   #start red led
    green.start((greenc/2.55)) #start green led
    blue.start((bluec/2.55))  #start blue led
