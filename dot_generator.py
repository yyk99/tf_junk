#!/usr/bin/eval python3
#

import matplotlib.pyplot as plt
import numpy as np

class dot_generator:
    def __init__(self):
        self._shape = (200,200)
        self._serial = 0
        self._dpi = 96
        np.random.seed(3)

    def generate_one(self):
        x = 4 + np.random.normal(0, 2, 24)
        y = 4 + np.random.normal(0, 2, len(x))
        # size and color:
        sizes = np.repeat(80, len(x))
        colors = np.repeat(250, len(x))

        # plt.figure(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi)
                
        fig, ax = plt.subplots()
        fig.set_dpi(self._dpi)
        fig.set_figwidth(self._shape[0]/self._dpi)
        fig.set_figheight(self._shape[0]/self._dpi)

        # plot
        plt.grid(False)
        plt.axis(False)
        
        ax.scatter(x, y, s=80, c="black")
        
        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8))
        
        #plt.show()
        self._serial += 1
        plt.savefig('sample_%d.png' % self._serial)

  
