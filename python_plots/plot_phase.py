import numpy as np
import matplotlib.pyplot as plt

sample_rate = 2e6
corr_size = 8192

sample_freq_in_file = sample_rate/corr_size
time_per_sample = 1/sample_freq_in_file

def center_data(data):
    avg = np.average(data)
    data = data - avg
    return data

data_hackrf = np.fromfile(open("data/phase_stability_hackrf.bin"), dtype=np.float32)
data_hackrf = center_data(data_hackrf[10000:])

data_kerberos = np.fromfile(open("data/kerberos_phase_stability.bin"), dtype=np.float32)
data_kerberos = center_data(data_kerberos[10000:])

data_hackrf_len = len(data_hackrf)
data_kerberos_len = len(data_kerberos)

t_hackrf = np.linspace(0, time_per_sample*data_hackrf_len, data_hackrf_len)
t_kerberos = np.linspace(0, time_per_sample*data_kerberos_len, data_kerberos_len)

plt.plot(t_hackrf, data_hackrf, t_kerberos, data_kerberos)
plt.grid()
plt.xlabel(r"$t\ (\mathrm{s})$")
plt.ylabel(r"$\Delta \Theta\ (\mathrm{rad})$")
plt.legend(["HackRF", "KerberosSDR"])

print(np.std(data_hackrf))
print(np.std(data_kerberos))

plt.show()
