from time import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from rplidar import RPLidar

PI = 3.1415926535

lidar = RPLidar('/dev/ttyUSB0', baudrate=115200)


def quality(scan):
    if len(scan) == 4:
        return scan[1]
    elif len(scan) == 3:
        return scan[0]
    else:
        return None

def angle(scan):
    if len(scan) == 4:
        return scan[2]
    elif len(scan) == 3:
        return scan[1]
    else:
        return None

def distance(scan):
    if len(scan) == 4:
        return scan[3]
    elif len(scan) == 3:
        return scan[2]
    else:
        return None
    
def good_quality(scan, min_q=10):
    q = quality(scan)
    if q is not None:
        return q > min_q
    return False

def angle_rad(scan):
    deg = angle(scan)
    return (PI * deg) / 180

def measurements_iterator():
    now = time()
    nb_meas = 0
    while (nb_meas < 10000):
        available = True
        measures = lidar.iter_measurments()

        while (available):
            try:
                meas = next(measures)
                # print(next(measures))
            except StopIteration:
                available = False
                print("end loop")
            else:
                if(good_quality(scan=meas, min_q=10)):
                    nb_meas += 1
                    if not (nb_meas % 100):
                        print(nb_meas, "    ", meas)
                        if (nb_meas >= 10000):
                            break
    duree = time() - now
    print("nb meas: ", nb_meas, " time: ", duree, " fps: ", nb_meas / duree / 360)

print(matplotlib.rcParams['backend'])

plt.axes(polar=True)
r = []
th = []

measurements = lidar.iter_measurments(100)

for i in range(1000):
    try:
        item = next(measurements)
    except StopIteration:
        print("error")
    else:
        if (good_quality(item, min_q=10)):
            r.append(distance(item))
            th.append(PI - angle_rad(item))


# measurements_iterator()

lidar.stop()
lidar.stop_motor()

plt.polar(th, r, "ro", markersize=4)
plt.show()

pass
