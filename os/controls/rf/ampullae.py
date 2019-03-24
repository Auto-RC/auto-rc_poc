# ==================================================================================================
#                                       GLOBAL IMPORTS
# ==================================================================================================

import smbus
import os
import sys
import time
from threading import Thread

# ==================================================================================================
#                                        LOCAL IMPORTS
# ==================================================================================================

current_dir = os.path.dirname(os.path.realpath(__file__))
sensors_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
parent_dir = os.path.abspath(os.path.join(sensors_dir, os.pardir))

utility_dir = parent_dir + r'/utility'
controls_dir = current_dir + r'/controls'

sys.path.append(utility_dir)
sys.path.append(controls_dir)

from logger import *

# ==================================================================================================
#                                           Ampullae
# ==================================================================================================

class Ampullae(Thread.thread):

    def __init__(self, address):

        # Main parameters
        # ------------------------------------------------------------------------------------------
        self.address = address

        self.i2c =

        self.throttle = 0
        self.steering = 0
        self.mode = 0


    def read(self):
        n = self.bus.read_byte(self.address)
        n_binary = bin(n)[2:]

        if n_binary[0] == 0 and n_binary[1] == 1:
            self.throttle = int(n[2:], 2)

        if n_binary[0] == 1 and n_binary[1] == 0:
            self.steering = int(n[2:], 2)

        if n_binary[0] == 1 and n_binary[1] == 1:
            self.mode = int(n[2:], 2)


    def get_current_picture(self):
        return self.cam.run_threaded()

    def stop(self):
        self.cam.shutdown()

        logger.info("Camera thread ended")


# ==================================================================================================
#                                            TEST CODE
# ==================================================================================================

if __name__ == '__main__':

    c = Iris(20, (128, 96), 'rgb')

    c.run()

    for i in range(10):
        print(c.get_current_picture())
        time.sleep(.5)

    c.stop()




