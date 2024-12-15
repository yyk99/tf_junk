#!/usr/bin/eval python3
#

import matplotlib.pyplot as plt
import numpy as np

class dot_generator:
    def __init__(self):
        self._shape = (200,200)
        self._serial = 0
        np.random.seed(3)

    def generate_one(self):
        x = 4 + np.random.normal(0, 2, 24)
        y = 4 + np.random.normal(0, 2, len(x))
        # size and color:
        sizes = np.random.uniform(80, 80, len(x))
        colors = np.random.uniform(250, 250, len(x))
                
        fig, ax = plt.subplots()
        # plot
        plt.grid(False)
        plt.axis(False)
        
        ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
        
        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8))
        
        #plt.show()
        self._serial += 1
        plt.savefig('sample_%d.png' % self._serial)

  
