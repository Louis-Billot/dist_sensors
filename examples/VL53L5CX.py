import time

from vl53l5cx.vl53l5cx import VL53L5CX

driver = VL53L5CX()

alive = driver.is_alive()
if not alive:
    raise IOError("VL53L5CX Device is not alive")

print("Initialising...")
t = time.time()
driver.init()
print(f"Initialised ({time.time() - t:.1f}s)")

driver.set_ranging_frequency_hz(10)

print(driver.get_integration_time_ms(), driver.get_ranging_frequency_hz())

t = time.time()
while time.time() - t < 5:
    pass


# Ranging:
driver.start_ranging()

previous_time = 0
loop = 0
while True:
# while loop < 10:
    if driver.check_data_ready():
        ranging_data = driver.get_ranging_data()

        # As the sensor is set in 4x4 mode by default, we have a total 
        # of 16 zones to print. For this example, only the data of first zone are 
        # print
        now = time.time()
        if previous_time != 0:
            time_to_get_new_data = now - previous_time
            print(f"Print data no : {driver.streamcount: >3d} ({time_to_get_new_data * 1000:.1f}ms)")
        else:
            print(f"Print data no : {driver.streamcount: >3d}")

        # for i in range(16):
        #     print(f"Zone : {i: >3d}, "
        #           f"Status : {ranging_data.target_status[driver.nb_target_per_zone * i]: >3d}, "
        #           f"Distance : {ranging_data.distance_mm[driver.nb_target_per_zone * i]: >4.0f} mm")

        for i in range(4):
            index = (driver.nb_target_per_zone * i * 4, 4 + driver.nb_target_per_zone * i *4)
            print('  '.join(["{: >10}".format(f"{d:.0f} {'#' if s !=255 else ' '}") for d, s in zip(ranging_data.distance_mm[index[0]:index[1]], ranging_data.target_status[index[0]:index[1]])]))
            # for j in range(4):
            #     print(ranging_data.distance_mm[driver.nb_target_per_zone * i * 4 + driver.nb_target_per_zone * j])
            # print(ranging_data.distance_mm[driver.nb_target_per_zone * i * 4 : 4 + driver.nb_target_per_zone * i *4])

        print(f"")

        previous_time = now
        loop += 1

    time.sleep(0.005)