import numpy as np
import matplotlib.pyplot as plt

def second_law_simulation(mass, force, t_max):
    t = np.linspace(0, t_max, 100)
    a = force / mass
    v = a * t
    x = 0.5 * a * t**2
    return t, a, v, x

def plot_second_law(t, a, v, x, mass, force):
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(t, v)
    plt.title("Velocity vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.grid(True)
    plt.subplot(1, 2, 2)
    plt.plot(t, x)
    plt.title("Position vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    plt.grid(True)
    plt.tight_layout()
    plt.suptitle(f"Newton's 2nd Law: m={mass} kg, F={force} N", y=1.05)
    plt.show()

def main():
    mass = float(input("Enter mass (kg): "))
    force = float(input("Enter net force (N): "))
    t_max = float(input("Enter total time (s): "))
    t, a, v, x = second_law_simulation(mass, force, t_max)
    plot_second_law(t, a, v, x, mass, force)

if __name__ == "__main__":
    main()
