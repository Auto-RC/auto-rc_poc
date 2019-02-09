# ==================================================================================================
#                                       GLOBAL IMPORTS
# ==================================================================================================

import os
import sys
import numpy as np
import datetime

# ==================================================================================================
#                                        LOCAL IMPORTS
# ==================================================================================================

from logger import *

# ==================================================================================================
#                                           IRIS
# ==================================================================================================

class Memory:

    def init_package(self, modules=[]):


        self.data_dir = '/dev/sda/data'
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

    def add(self, data_packet):

        for module in self.modules:
            self.data_package[module].append(data_packet[module])

    def save(self):

        for module in self.modules:
            np.save("{}/{}-{}".format(self.data_dir, module,self.timestamp),
                    np.array(self.data_package[module]))

# ==================================================================================================
#                                            TEST CODE
# ==================================================================================================

if __name__ == '__main__':

    mem = Memory(modules=['camera'])

    data_packet = dict()
    data_packet['camera'] = [1]

    mem.add(data_packet)

    mem.save()
