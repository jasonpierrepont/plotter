import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter, PillowWriter
import random

# plt.rcParams['animation.ffmpeg_path'] = 'path to ffmpeg'

fig = plt.figure()
(l,) = plt.plot([], [], "k-")
(l2,) = plt.plot([], [], "m--")

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.title("Title")


def func(x):
    return np.sin(x) * 3


def func2(x):
    return np.cos(x) * 3


metadata = {"title": "Movie", "artist": "codinglikemad"}
# writer = PillowWriter(fps=15, metadata=metadata)
writer = FFMpegWriter(fps=15, metadata=metadata)

xlist = []
ylist = []
ylist2 = []

filepath = "sinWave.gif"
filepath = "sinWave.mp4"

with writer.saving(fig, filepath, 100):
    for xval in np.linspace(-5, 5, 100):
        xlist.append(xval)
        ylist.append(func(xval))
        ylist2.append(func2(xval))

        l.set_data(xlist, ylist)
        l2.set_data(xlist, ylist2)
        writer.grab_frame()

