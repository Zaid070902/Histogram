import matplotlib.pyplot as plt

x = [0.5, 0.7, 1.1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

ax = plt.axes()
ax.set_facecolor("#111")
plt.title("Histogram of nums against bins")
plt.xlabel("Nums")
plt.ylabel("Bins")
plt.hist(x, bins, color="#111", edgecolor="cyan")
plt.show()
