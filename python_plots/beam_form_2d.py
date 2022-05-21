import numpy as np
from matplotlib import pyplot as plt

def calculate_array_factor(az, el, phase, freq, spacing, n = 2):
    '''
    Calculates array factored base on formula (12) from
    https://www.analog.com/en/analog-dialogue/articles/phased-array-antenna-patterns-part1.html

    beam_angles - np array of beam_angles (rad)
    freq - signal frequency
    spacing - distance between antennas
    phase - phase shift of antenna elements (rad)
    '''
    c = 299792458
    d = spacing
    lam = c/freq

    x = np.pi * np.sin(el) * np.cos(az)
    y = np.pi * np.sin(el) * np.sin(az)

    def af_1d(m, x):
        return (1/m)*np.sin(m/2 * x)/np.sin(x/2)

    af = af_1d(n, x) * af_1d(n, y)
    return af


azimuth_angles = np.linspace(-np.pi, np.pi, 500)
elevation_angles = np.linspace(0, np.pi/2, 500)

az, el = np.meshgrid(azimuth_angles, elevation_angles)

# n = [2, 4, 8, 16]
n = [4]
af = []

for idx in n:
    af.append(calculate_array_factor(az, el, np.deg2rad(0), 1575.42e6, 0.095, idx))

fig = plt.figure()
from mpl_toolkits.mplot3d import Axes3D
ax = Axes3D(fig)
plt.subplot(projection="polar")
# ax.plot_surface(az, np.rad2deg(el), af[0])
plt.pcolormesh(az, np.rad2deg(el), af[0])
plt.grid()

# plt.polar(np.degrees(beam_angles), np.log10(np.abs(af))*32)
# fig,ax = plt.subplots(subplot_kw={'projection': 'polar'} )
# for idx, n_val in enumerate(n):
#     ax.plot(beam_angles, np.log10(np.abs(af[idx]))*10, label="N = {}".format(n_val))
# ax.set_thetamax(90)
# ax.set_thetamin(-90)
# ax.set_theta_offset(0.5*np.pi)

# r_label = ax.set_ylabel(r"$\Theta\ (\mathrm{deg})$")
# r_label.set_position((1.0, 0.7))
# r_label.set_rotation(0)
# # label2 = ax.set_xlabel("AF (dB)")
# # label2.set_position((0.8, -2))
# plt.text(.8, .14, "AF (dB)", transform=ax.transAxes)

# ax.legend()
# plt.yscale('log')
plt.show()


