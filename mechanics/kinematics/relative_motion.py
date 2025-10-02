def relative_velocity(v_a, v_b):
    """
    Calculate the relative velocity of object A with respect to object B.
    Args:
        v_a (tuple): Velocity of object A (vx, vy)
        v_b (tuple): Velocity of object B (vx, vy)
    Returns:
        tuple: Relative velocity (vx, vy)
    """
    return (v_a[0] - v_b[0], v_a[1] - v_b[1])

def main():
    print("Enter velocity of object A (vx vy): ", end="")
    v_a = tuple(map(float, input().split()))
    print("Enter velocity of object B (vx vy): ", end="")
    v_b = tuple(map(float, input().split()))
    v_rel = relative_velocity(v_a, v_b)
    print(f"Relative velocity of A with respect to B: {v_rel[0]:.2f} m/s, {v_rel[1]:.2f} m/s")

if __name__ == "__main__":
    main()
