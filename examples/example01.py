import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter, PillowWriter
import random


x_values = []
y_values = []

for _ in range(100):
    x_values.append(random.randint(0, 100))
    y_values.append(random.randint(0, 100))

    plt.xlim(0, 100)
    plt.ylim(0, 100)
    # this rebuilds the whole plot each loop, is there a better way???
    plt.scatter(x_values, y_values, color="black")
    plt.pause(0.001)

plt.show()
