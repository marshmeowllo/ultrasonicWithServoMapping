# ultrasonicWithServoMapping ![love](http://ForTheBadge.com/images/badges/built-with-love.svg) ![python](http://ForTheBadge.com/images/badges/made-with-python.svg)
> :warning:This project is not finished yet. So there might be some problems. If you find it, please inform me. Thank you.
<br>
This project is a long term project made to create 3D model from distance sensor and camera.
<br>
This project is baseed on ESP8266.

## requirement
- ESP8266
- Servo MG90S (I recommend using a more efficient servo.)
- HC-SR04 Ultrasonic Sensor
- OLED Display 0.96 inch
- library
  - [servo.py](https://github.com/pvanallen/esp32-getstarted/blob/master/examples/servo.py)
  - [hcsr04.py](https://raw.githubusercontent.com/RuiSantosdotme/Random-Nerd-Tutorials/master/Projects/ESP-MicroPython/HCSR04/hcsr04.py)
  - [ssd1306.py](https://raw.githubusercontent.com/RuiSantosdotme/ESP-MicroPython/master/code/Others/OLED/ssd1306.py)

## Connecting

### OLED Display
| OLED  | ESP8266 |
| ------------- | ------------- |
| Vin  | 3.3V  |
| GND  | GND  |
| SCL  | GPIO 5 or (D1)  |
| SDA  | GPIO 4 or (D2)  |

### HC-SR04 Ultrasonic Sensor
| HC-SR04  | ESP8266 |
| ------------- | ------------- |
| VCC  | VIN  |
| Trig  | GPIO 12 or (D6)  |
| Echo  | GPIO 14 or (D5)  |
| GND  | GND  |

### Servo Motor
| HC-SR04  | ESP8266 |
| ------------- | ------------- |
| Ground (Brown)  | GND  |
| Power (Red)  | Vin  |
| Signal (Orange/Yellow)  | GPIO 13 or (D7)  |

## Result
The results were found to be highly inaccurate. I highly recommend that if there is a device that performs better than that, I have recommended, use it.
<br>
![plot.png](./img/plot.png)
<img src="https://github.com/marshmeowllo/laughing-octo-tribble/blob/main/img/servo.gif" width="20%" height="20%">
<img src="https://github.com/marshmeowllo/laughing-octo-tribble/blob/main/img/oled.gif" width="20%" height="20%">

## reference

- [HC-SR04](https://randomnerdtutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/)
- [OLED](https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/)
- [Servo1](http://techawarey.com/programming/micropython/servo-motor-control-using-micropython/)
- [Servo2](https://github.com/pvanallen/esp32-getstarted/blob/master/docs/servo.md)
