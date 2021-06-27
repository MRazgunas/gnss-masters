import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

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


n = 4

beam_angles = np.linspace(-np.pi/2, np.pi/2, 5000)

fig,ax = plt.subplots(subplot_kw={'projection': 'polar'} )
af = calculate_array_factor(beam_angles, np.deg2rad(0), 1575.42e6, 0.095, n)
line, = ax.plot(beam_angles, np.log10(np.abs(af))*10)

ax.set_thetamax(90)
ax.set_thetamin(-90)
ax.set_theta_offset(0.5*np.pi)


r_label = ax.set_ylabel(r"$\Theta\ (\mathrm{deg})$")
r_label.set_position((1.0, 0.7))
r_label.set_rotation(0)
# label2 = ax.set_xlabel("AF (dB)")
# label2.set_position((0.8, -2))
plt.text(.8, .14, "AF (dB)", transform=ax.transAxes)
plt.yticks(np.arange(-40, 0+1, 10))

time_text = ax.text(-0.5, 0, '')
ax.legend()

# fig.set_size_inches(h_in_inches, w_in_inches)

def animate(i):
    af = calculate_array_factor(beam_angles, np.deg2rad(i), 1575.42e6, 0.095, n)
    line.set_ydata(np.log10(np.abs(af))*10)
    time_text.set_text(r"$\Delta \Phi = " + str(i) + r"\ \mathrm{(deg)}$")
    return line,time_text,

ani = animation.FuncAnimation(
    fig, animate, interval=50, frames=180, blit=True
)

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

ani.save('im.mp4', writer=writer, dpi=100)

# plt.show()


