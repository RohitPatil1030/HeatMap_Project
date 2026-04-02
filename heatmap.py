import numpy as np
import matplotlib.pyplot as plt

# Create grid
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)

# Temperature function (scalar field)
T = np.sin(X) * np.cos(Y)

# Plot heat map
plt.figure()
plt.imshow(T, extent=[0,5,0,5], origin='lower')
plt.colorbar(label='Temperature')
plt.title("Heat Map Visualization")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.savefig("output.png")
plt.show()

# Approximate double integration (total heat)
total_heat = np.trapz(np.trapz(T, x), y)

print("Total Heat:", total_heat)