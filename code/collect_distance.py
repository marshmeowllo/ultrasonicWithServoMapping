from hcsr04 import HCSR04
from machine import Pin, SoftI2C
import ssd1306
from servo import Servo
from time import sleep

#ultrasonic sensor
sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

#servo
servo_pin = Pin(13)
my_servo = Servo(servo_pin)
delay = 0.5

#oled display
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

my_servo.write_angle(0)
i=0
while True:
    try:
        oled.fill(0)
        #distance calculator
        distance = sensor.distance_cm()
        print('Distance:', distance, 'mm')
        oled.text('Alogorimeow', 0, 10)
        oled.text('Current Distance', 0, 30)
        oled.text(str(distance)+' mm' , 0, 40)
        oled.show()
        if i<=180:
            my_servo.write_angle(i)
            i=i+5
        else:
            #finish process and show in oled display
            oled.fill(0)
            oled.text('finished' , 0, 30)
            oled.show()
            sleep(1)
            oled.fill(1)
            oled.show()
            sleep(1)
            oled.fill(0)
            oled.show()
            
            #reset servo angle
            my_servo.write_angle(0)
            break
        sleep(1)
    except OSError as ex:
        print('ERROR getting distance:', ex)
        oled.fill(0)
        oled.text('Alogorimeow', 0, 10)
        oled.text(str(ex), 0, 10)
        oled.show()
    

