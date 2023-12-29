# This is an approximation of Python code

import time
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.set_drone_LED(255, 0, 255, 255)
drone.takeoff()
drone.hover(0.5)
print(drone.get_height("m"))
print(drone.get_pressure("Pa"))
for count in range(8):
  drone.set_roll(0)
  drone.set_pitch(0)
  drone.set_yaw(0)
  drone.set_throttle(10)
  drone.move(1.00)
  drone.hover(0.5)
  print(drone.get_height("m"))
  print(drone.get_pressure("Pa"))
drone.land()

drone.close()