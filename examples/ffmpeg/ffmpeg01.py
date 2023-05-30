"""Generate raw RGB frames and feed them to ffmpeg stdin"""
import subprocess as sp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter, PillowWriter

width, height = 640, 480
dpi = 100

ffmpeg_exe = "ffmpeg"
cmd = [
    ffmpeg_exe,
    "-f",
    "rawvideo",
    "-video_size",
    f"{width}x{height}",
    "-pixel_format",
    "rgb24",
    "-i",
    "pipe:",
    "-c:v",
    "libx264",
    "stdin_test.mp4",
]

pipe_in = sp.PIPE
p = sp.Popen(cmd, stdin=pipe_in)

plt.ioff()
fig = plt.figure()
(l,) = plt.plot([], [], "k-")
(l2,) = plt.plot([], [], "m--")

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.title("Title")
fig.set_dpi = dpi
fig.set_figwidth(width / dpi)
fig.set_figheight(height / dpi)


def func(x):
    return np.sin(x) * 3


def func2(x):
    return np.cos(x) * 3


xlist = []
ylist = []
ylist2 = []

print("starting loop")
for i, xval in enumerate(np.linspace(-5, 5, 100), start=1):
    xlist.append(xval)
    ylist.append(func(xval))
    ylist2.append(func2(xval))

    l.set_data(xlist, ylist)
    l2.set_data(xlist, ylist2)
    fig.canvas.draw()
    data = fig.canvas.tostring_rgb()
    print(
        f"Frame {i:03d}  {type(data)}  size: {len(data)} expected size: {width * height * 3}"
    )

    # assert len(data) == (width * height * 3)
    p.stdin.write(data)


p.stdin.write(b"")
print("Done writing")
p.communicate()

# p.wait(timeout=30)
print(f"Return code: {p.returncode}")
