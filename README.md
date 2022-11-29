# Repo for tests and benchmarks of distance sensors

The selected sensors are the following:
- generic HC-SR05 ultrasonic sensor (PWM output)
- DFRobot URM09 ultrasonic sensor (I2C output)
- VL53L4CX single chip lidar sensor (I2C output)
- VL53L5CX single chip lidar sensor with 8x8 multi-zone (I2C output)
- DFRobot SEN0413 medium range lidar sensor (UART & I2C output)
- TFLUNA medium range lidar sensor (UART & I2C output)

The RPLIDAR rotating LiDAR <!-- TODO: from ... --> is used to map the benchmark room

A benchmark of the depth sensing capabilities of the OAK-D Lite camera is also executed

## Setup procedures

See the [SETUP.md](./SETUP.md) file for sensor specific procedures

## Examples

See the [./examples/](./examples/) folder for simple usage example of a given sensor

## Benchmarks
<!-- TODO -->
WIP

## Raspberry Pi 4 pinout

![RPi4 pinout](./assets/R-Pi-4-GPIO-Pinout.jpg)

