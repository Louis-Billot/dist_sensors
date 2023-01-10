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
WIP

Pas de dégradation notable des mesures lorsque les 4 capteurs sont utilisés en même temps (sur la même cible)
Pour tous les capteurs, il est conseillé de s'assurer que la cible mesurée occupe l'entièreté du champ de vision du capteur afin que la mesure soit correcte. Si plusieurs distances différentes sont observables dans le champ de vision d'un capteur, celui-ci pourra renvoyer une distance aléatoire comprise entre les différentes distances. Il n'y a pas d'indicateur permettant de s'assurer de la validité de la mesure, un filtre doit être implémenté

TODO: Tableau de compatibilité avec les cartes

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

La librairie CircuitPython considère le capteur comme étant le VL53L4CD et donc la plage de détection est réduite à 1.3m
ST fourni l'API en C et une implémentation pour Arduino existe mais requière suffisamment de mémoire RAM et FLASH ! (les ATMega328P sont donc exclus!)
néons -> range maximale pour le blanc; 1m10 pour le foncé
spots -> max 1m20 pour du blanc et max 1m pour du foncé

### VL53L5CX
WIP

> This sensor is a single chip sensor tested on a module adding only power regulation from 5V -> 3V3 all results are valid for the sensor chip in itself.

> I2C Communication library officially available in C from [ST](https://www.st.com/en/embedded-software/stsw-img023.html). Multiple Python implementations are available on GitHub, [this is the one used for the tests](https://github.com/Abstract-Horizon/vl53l5cx_python). An [STM32duino port](https://github.com/stm32duino/VL53L5CX) is also available.

noir -> 3m50 pour le blanc, 3m pour le foncé
néons -> 3m pour le blanc, 2m5 pour le foncé
spots -> 1m5 pour le blanc, 1m pour le foncé
le capteur indique si le statut de la mesure est correct ou pas. la dernière mesure correcte est gardée en mémoire tant qu'une nouvelle mesure valide ne l'a pas remplacée
l'effet de l'angle d'incidence est faiblement perceptible (tant que l'angle reste correct, généralement à partir de 45° la mesure ne se fait plus)
Ce capteur renvoie une valeur de statut pour chacune des mesures indiquant sa confiance dans la mesure.

### DFRobot SEN0413
WIP

> This sensor is a complete module with multiple chips, it is not possible to evaluate the sensor only performances.

> I2C communication protocol is available in the [sensor datasheet](https://dfimg.dfrobot.com/nobody/wiki/1840a7b7b14e02f3566e0cef5b51e9ba.pdf)

Pas de changement notable dans une portée de 6m malgré les changements de luminosité (néons/spots/noir), les changements de réflfectivité, l'angle d'incidence (dans la limite du correct)
NOTE: le sensor peut automatiquement modifier sa fréquence d'acquisition pour faire une moyenne sur plus de valeurs et améliorer la détection lorsque les conditions se déterriorent
Uniquement une librairie Arduino (en C++) donc demande du dev pour implémenter la librairie en se basant sur la datasheet.

### TFLUNA
WIP

> This sensor is a complete module with multiple chips, it is not possible to evaluate the sensor only performances.

> I2C register table is available in the [sensor datasheet](https://www.gotronic.fr/pj2-sj-pm-tf-luna-a03-product-manual-2195.pdf#page=28&zoom=100,53,130)

noir/ néons -> pas de changement 
néons/spots -> pas de changement
néons/lumière du jour -> perte de range notoire max 3 à 5m
réflectivité -> pas de changement lorsque orthogonal mais perte de la mesure dès que l'angle dépasse quelques degrés (pour une feuille noire) alors qu'avec une feuille blanche, la mesure reste correcte jusqu'à 45° passé [lorsque plus de 2,5m]

La cible doit occuper l'entièreté du FOV du LiDAR pour que la mesure soit valide (2° de FOV -> à 8m la cible doit faire ~28cm de diamètre)

<!-- TODO: Check frequency -->

### RPLIDAR
WIP

### OAK-D Lite
WIP
