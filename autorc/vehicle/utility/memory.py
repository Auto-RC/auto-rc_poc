# ==================================================================================================
#                                       GLOBAL IMPORTS
# ==================================================================================================

import os
import sys
import numpy as np
import datetime
import time
import logging

# ==================================================================================================
#                                            LOGGER SETUP
# ==================================================================================================

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logger.setLevel(logging.INFO)

# ==================================================================================================
#                                           IRIS
# ==================================================================================================

class Memory:

    def __init__(self, modules=[]):


        self.data_dir = '/home/pi/data'
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)


        # Initializing a key in data package for every module in modules
        # ------------------------------------------------------------------------------------------
        self.modules = modules
        self.data_package = dict()
        for module in self.modules:
            self.data_package[module] = []

        self.timestamp = datetime.datetime.now()
        logger.debug('Created a data package at {}'.format(self.timestamp))

        time.sleep(0.5)

    def add(self, data_packet):

        for module in self.modules:
            self.data_package[module].append(data_packet[module])

    def save(self):

        for module in self.modules:
            np.save("{}/{}-{}".format(self.data_dir, module,str(self.timestamp).replace(":",";")),
                    np.array(self.data_package[module]))



# ==================================================================================================
#                                            UNIT TEST
# ==================================================================================================

if __name__ == '__main__':

    mem = Memory(modules=['camera'])

    data_packet = dict()
    data_packet['camera'] = [1]

    mem.add(data_packet)

    mem.save()
