import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot([1,2,3])
ax2 = fig.add_subplot(332, facecolor = 'y')
ax2.plot([1,2,3])
plt.show()