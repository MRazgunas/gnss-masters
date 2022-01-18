import numpy as np
import matplotlib.pyplot as plt

# from scipy import signal

import pickle

vec_len = 1024*8
samp_rate = 1e6

data = np.fromfile("data/hackrf_correlation.bin", np.complex64)

data = data[vec_len*9:vec_len*10]
print(np.argmax(np.abs(data)))
data = np.fft.fftshift(data)
data = np.abs(data)
delta_t = (1/samp_rate)*1e6
time_len = vec_len*delta_t
t1 = np.linspace(-(time_len)/2, (time_len)/2-delta_t, num=vec_len)

fig, ax = plt.subplots()

ax.plot(t1, data, "-*")

ax.tick_params(axis="y",direction="in")
ax.tick_params(axis="x",direction="in")

plt.xlabel(r"$t\ (\mu s)$")
# plt.ylabel(r"$\Delta \Phi\ (rad)$")

plt.grid()
plt.xlim([-100, 100])
plt.show()
