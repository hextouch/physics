import numpy as np

def inclined_plane(mass, angle_deg, mu_k=0, g=9.81):
    angle_rad = np.radians(angle_deg)
    weight = mass * g
    normal = weight * np.cos(angle_rad)
    friction = mu_k * normal
    down_slope = weight * np.sin(angle_rad)
    net_force = down_slope - friction
    a = net_force / mass if net_force > 0 else 0
    return a, friction, normal

def main():
    mass = float(input("Enter mass (kg): "))
    angle = float(input("Enter incline angle (degrees): "))
    mu_k = float(input("Enter coefficient of kinetic friction (0 for none): "))
    a, friction, normal = inclined_plane(mass, angle, mu_k)
    print(f"Acceleration down the plane: {a:.2f} m/s²")
    print(f"Friction force: {friction:.2f} N")
    print(f"Normal force: {normal:.2f} N")

if __name__ == "__main__":
    main()
