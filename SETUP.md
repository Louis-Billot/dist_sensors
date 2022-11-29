# Hardware and software setup
The hardware connections and software setup are available for the following sensors:
- [HC-SR05](#hc-sr05)
- [DFRobot URM09](#dfrobot-urm09)
- [VL53L4CX](#vl53l4cx)
- [VL53L5CX](#vl53l5cx)
- [DFRobot SEN0413](#dfrobot-sen0413)
- [TFLUNA](#tfluna)
- [RPLIDAR](#rplidar)
- [OAK-D Lite](#oak-d-lite)

Links to [additional resources](#other-resources) are available at the bottom of this document.

## HC-SR05
#### Pin connections:
- Trigger pin -> GPIO23
- Echo pin -> GPIO24 (through a resistor divider to accomodate de 3V3 level of the RaspberryPi)

#### Python virtual environment setup:
~~~~bash
python3.9 -m venv venvHCSR05
pip install -U pip
pip install wheel
pip install RPi.GPIO
~~~~

#### Common errors:
- make sure your user is in the `gpio` group
- install the dev package of your python version (for example `python3.9-dev`)
- you may need to install `rpi.gpio-common` in Ubuntu

## DFRobot URM09
#### Python virtual environment setup:
~~~~bash
python3.9 -m venv venvURM09
pip install -U pip
pip install wheel
~~~~

## VL53L4CX
WIP

## VL53L5CX
WIP

## DFRobot SEN0413
WIP

## TFLUNA
WIP

## RPLIDAR
WIP

## OAK-D Lite
WIP

## Other Resources
- [ThePiHut tutorial](https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)
- [GPIO setup on Ubuntu before 21.04](https://forums.raspberrypi.com/viewtopic.php?t=289084#p1748054)
- [GPIO setup on Ubuntu after 21.04](https://ubuntu.com/tutorials/gpio-on-raspberry-pi#1-overview)
- [Enable I2C on RaspiOS](https://pi3g.com/2021/05/20/enabling-and-checking-i2c-on-the-raspberry-pi-using-the-command-line-for-your-own-scripts/)
