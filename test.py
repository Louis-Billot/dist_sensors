# import matplotlib
# import matplotlib.pyplot as plt
# print(matplotlib.rcParams['backend'])

# temp = [i*i for i in range(10)]
# plt.plot(temp)
# plt.show(block=False)

# exit()

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from rplidar import RPLidar

def get_data():
    lidar = RPLidar('/dev/ttyUSB0', baudrate=115200)
    for scan in lidar.iter_scans(max_buf_meas=500):
        break
    lidar.stop()
    return scan

print(matplotlib.rcParams['backend'])

for i in range(10):
    if(i%7==0):
        x = []
        y = []
    print(i)
    current_data=get_data()
    for point in current_data:
        if point[0]==15:
            angle = np.deg2rad(point[1])
            x.append(point[2]*np.sin(angle))
            y.append(point[2]*np.cos(angle))
    plt.clf()
    plt.scatter(x, y)
    plt.pause(.1)
plt.show()