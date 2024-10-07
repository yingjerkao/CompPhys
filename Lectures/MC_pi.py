import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to estimate pi and animate the process
def estimate_pi(num_samples):
    inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    estimates = []

    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Monte Carlo Estimation of π")

    inside_points, = ax.plot([], [], 'bo', markersize=1, label="Inside Circle")
    outside_points, = ax.plot([], [], 'ro', markersize=1, label="Outside Circle")

    def update(frame):
        nonlocal inside_circle

        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            x_inside.append(x)
            y_inside.append(y)
            inside_circle += 1
        else:
            x_outside.append(x)
            y_outside.append(y)

        # Update the estimate of pi
        if frame > 0:
            pi_estimate = (inside_circle / frame) * 4
            estimates.append(pi_estimate)

        inside_points.set_data(x_inside, y_inside)
        outside_points.set_data(x_outside, y_outside)

        # Set the plot title with the current estimate of pi
        ax.set_title(f"Monte Carlo Estimation of π\nEstimate: {pi_estimate:.6f}")

        return inside_points, outside_points

    ani = animation.FuncAnimation(fig, update, frames=range(1, num_samples + 1),
                                  interval=1, blit=True, repeat=False)

    plt.legend()
    plt.show()

# Example usage
num_samples = 1000
estimate_pi(num_samples)
