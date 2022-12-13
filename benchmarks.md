# Distance Sensor Benchmarks

## Sensors list
- [HC-SR05](#hc-sr05)
- [DFRobot URM09](#dfrobot-urm09)
- [VL53L4CX](#vl53l4cx)
- [VL53L5CX](#vl53l5cx)
- [DFRobot SEN0413](#dfrobot-sen0413)
- [TFLUNA](#tfluna)
- [RPLIDAR](#rplidar)
- [OAK-D Lite](#oak-d-lite)

## Setups

## Results

### HC-SR05
WIP

> This sensor was tested as a module. It is composed of a transducer and a receiver that have the same reference and some analogic circuitry. Its is not possible to evaluate a single chip as there exist many variations depending on the manufacturer.

## DFRobot URM09
WIP

> This sensor was tested as a module. It is composed of a transducer and a receiver that have the same reference and some analogic circuitry as well as a small microcontroller (STM 8bits) to convert the signals to digital and manage the I2C communication.

> I2C Communication library available in C++ and Python on [GitHub/DFRobot_URM09](https://github.com/DFRobot/DFRobot_URM09)

### VL53L4CX
WIP

> This sensor is a single chip sensor tested on a module adding only power regulation from 5V -> 3V3 all results are valid for the sensor chip in itself.

> I2C Communication library officially available in C from [ST](https://www.st.com/content/st_com/en/products/embedded-software/imaging-software/stsw-img029.html). An [STM32duino port](https://github.com/stm32duino/VL53L4CX) is also available. This sensor does not seem as popular as there is no Python port or wrapper of the library. There is a [CircuitPython library](https://github.com/adafruit/Adafruit_CircuitPython_VL53L4CD) from Adafruit but it is intented for the VL53L4CD sensor. 

### VL53L5CX
WIP

> This sensor is a single chip sensor tested on a module adding only power regulation from 5V -> 3V3 all results are valid for the sensor chip in itself.

> I2C Communication library officially available in C from [ST](https://www.st.com/en/embedded-software/stsw-img023.html). Multiple Python implementations are available on GitHub, [this is the one used for the tests](https://github.com/Abstract-Horizon/vl53l5cx_python). An [STM32duino port](https://github.com/stm32duino/VL53L5CX) is also available.

### DFRobot SEN0413
WIP

> This sensor is a complete module with multiple chips, it is not possible to evaluate the sensor only performances.

> I2C communication protocol is available in the [sensor datasheet](https://dfimg.dfrobot.com/nobody/wiki/1840a7b7b14e02f3566e0cef5b51e9ba.pdf)

### TFLUNA
WIP

> This sensor is a complete module with multiple chips, it is not possible to evaluate the sensor only performances.

> I2C register table is available in the [sensor datasheet](https://www.gotronic.fr/pj2-sj-pm-tf-luna-a03-product-manual-2195.pdf#page=28&zoom=100,53,130)

### RPLIDAR
WIP

### OAK-D Lite
WIP
