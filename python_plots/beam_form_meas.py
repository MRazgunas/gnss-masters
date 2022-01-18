import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def process_csv_data(data):
    data = data.sort_values(by="angle (deg)")
    data["angle (rad)"] = np.deg2rad(data["angle (deg)"])
    return data


single_ant = process_csv_data(pd.read_csv("data/single_antenna_form.csv"))
dual_ant_no_phase = process_csv_data(pd.read_csv("data/dual_antenna_fi_0.csv"))
dual_ant_phase = process_csv_data(pd.read_csv("data/dual_antenna_fi_-2.02_target_dir_40_deg copy.csv"))

print(single_ant)



# beam_angles = np.linspace(-np.pi/2, np.pi/2, 5000)

# plt.polar(np.degrees(beam_angles), np.log10(np.abs(af))*32)
fig,ax = plt.subplots(subplot_kw={'projection': 'polar'} )
ax.plot(single_ant["angle (rad)"], single_ant["power (dB)"], label="$N=1$")
ax.plot(dual_ant_no_phase["angle (rad)"], dual_ant_no_phase["power (dB)"], label="$N=2,\ \Theta=0$")
ax.plot(dual_ant_phase["angle (rad)"], dual_ant_phase["power (dB)"], label="$N=2,\ \Theta=2,02$")
# for idx, n_val in enumerate(n):
#     ax.plot(beam_angles, np.log10(np.abs(af[idx]))*10, label="N = {}".format(n_val))
ax.set_thetamax(90)
ax.set_thetamin(-90)
ax.set_theta_offset(0.5*np.pi)

r_label = ax.set_ylabel(r"$\Theta\ (\mathrm{deg})$")
r_label.set_position((1.0, 0.7))
r_label.set_rotation(0)
# label2 = ax.set_xlabel("AF (dB)")
# label2.set_position((0.8, -2))
plt.text(.8, .14, "P (dB)", transform=ax.transAxes)

ax.legend()
# plt.yscale('log')
plt.show()
