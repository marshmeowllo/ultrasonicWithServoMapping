from hcsr04 import HCSR04
from machine import Pin, SoftI2C
import ssd1306
from time import sleep

sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    try:
        oled.fill(0)
        distance = sensor.distance_cm()
        print('Distance:', distance, 'mm')
        oled.text('Alogorimeow', 0, 10)
        oled.text('Current Distance', 0, 30)
        oled.text(str(distance)+' mm' , 0, 40)
        oled.show()
        sleep(1)
    except OSError as ex:
        print('ERROR getting distance:', ex)
        oled.fill(0)
        oled.text('Alogorimeow', 0, 10)
        oled.text(str(ex), 0, 10)
        oled.show()
    

