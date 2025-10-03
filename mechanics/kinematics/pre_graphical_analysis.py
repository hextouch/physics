import matplotlib.pyplot as plt
import numpy as np

def plot_motion_graphs():
    t = np.linspace(0, 10, 100)
    x = 2 * t + 3
    v = np.full_like(t, 2)
    a = np.zeros_like(t)
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(t, x)
    plt.title('Position vs Time')
    plt.ylabel('x (m)')
    plt.subplot(3, 1, 2)
    plt.plot(t, v)
    plt.title('Velocity vs Time')
    plt.ylabel('v (m/s)')
    plt.subplot(3, 1, 3)
    plt.plot(t, a)
    plt.title('Acceleration vs Time')
    plt.ylabel('a (m/s²)')
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_motion_graphs()
