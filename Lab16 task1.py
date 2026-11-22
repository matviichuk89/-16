import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 100)
y= np.sin(np.pi + x) + 0.1 * np.cos(x)
plt.plot(x, y, linestyle="--", color="lightblue", marker="s")

plt.savefig(r"C:\Users\Nazar\OneDrive\Desktop\Lab16_task1.png")
plt.show()