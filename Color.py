# This is an approximation of Python code

import time
from codrone_edu.drone import *

drone = Drone()
drone.pair()

color = None


drone.takeoff()
drone.land()
while drone.code_is_running():

color_data = drone.get_color_data()
  color = drone.predict_colors(color_data)[0]
  print(color)
  if color == ("Green"):
    drone.set_drone_LED(0, 255, 0, 255)
  elif color == ("Blue"):
    drone.set_drone_LED(25, 116, 210, 255)
  elif color == ("White"):
    drone.set_drone_LED(255, 255, 255, 255)
  elif color == ("Red"):
    drone.set_drone_LED(255, 0, 0, 255)
  elif color == ("Yellow"):
    drone.set_drone_LED(255, 255, 0, 255)
  elif color == ("LightBlue"):
    drone.set_drone_LED(172, 229, 238, 255)
  elif color == ("Purple"):
    drone.set_drone_LED(255, 0, 255, 255)
  elif color == ("Black"):
    drone.set_drone_LED(0, 0, 0, 255)

drone.close()