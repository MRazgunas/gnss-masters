import matplotlib.pyplot as plt

l = 0.1902937

x = [-l/2, -l/2, l/2, l/2]
y = [-l/2, l/2, -l/2, l/2,]

plt.scatter(x, y)
plt.grid()
plt.xlabel("$x\ (\mathrm{m})$")
plt.ylabel("$y\ (\mathrm{m})$")
plt.show()