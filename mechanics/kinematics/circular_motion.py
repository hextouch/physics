import numpy as np
import matplotlib.pyplot as plt

def circular_motion(r, omega, t_max):
    t = np.linspace(0, t_max, 200)
    x = r * np.cos(omega * t)
    y = r * np.sin(omega * t)
    return t, x, y

def plot_circular_motion(x, y, r, omega):
    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.title(f"Uniform Circular Motion: r={r} m, ω={omega} rad/s")
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def main():
    r = float(input("Enter radius (m): "))
    omega = float(input("Enter angular velocity (rad/s): "))
    t_max = float(input("Enter total time (s): "))
    t, x, y = circular_motion(r, omega, t_max)
    plot_circular_motion(x, y, r, omega)

if __name__ == "__main__":
    main()
