from rplidar import RPLidar

lidar = RPLidar('/dev/ttyUSB0', baudrate=115200)

lidar.stop()
lidar.stop_motor()

pass
