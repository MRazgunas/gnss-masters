import numpy as np
from matplotlib import pyplot as plt

def calculate_array_factor(beam_angles, phase, freq, spacing, n = 2):
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
    af = np.sin(n*((np.pi*d/lam)*np.sin(beam_angles) - phase/2))/(n * np.sin((np.pi*d/lam)*np.sin(beam_angles) - phase/2))
    return af


beam_angles = np.linspace(-np.pi/2, np.pi/2, 5000)

n = [2, 4, 8, 16]
af = []

for idx in n:
    af.append(calculate_array_factor(beam_angles, np.deg2rad(0), 1575.42e6, 0.095, idx))

# plt.polar(np.degrees(beam_angles), np.log10(np.abs(af))*32)
fig,ax = plt.subplots(subplot_kw={'projection': 'polar'} )
for idx, n_val in enumerate(n):
    ax.plot(beam_angles, np.log10(np.abs(af[idx]))*10, label="N = {}".format(n_val))
ax.set_thetamax(90)
ax.set_thetamin(-90)
ax.set_theta_offset(0.5*np.pi)

r_label = ax.set_ylabel(r"$\Theta\ (\mathrm{deg})$")
r_label.set_position((1.0, 0.7))
r_label.set_rotation(0)
# label2 = ax.set_xlabel("AF (dB)")
# label2.set_position((0.8, -2))
plt.text(.8, .14, "AF (dB)", transform=ax.transAxes)

ax.legend()
# plt.yscale('log')
plt.show()


