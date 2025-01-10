import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from Z_groups import *

def draw_dots_and_arrows(n, connections, window_title):
    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')

    # Set the window title
    fig.canvas.manager.set_window_title(window_title)

    # Calculate dot positions (starting from top, going clockwise)
    angles = np.linspace(np.pi / 2, -3 * np.pi / 2, n, endpoint=False)
    x = np.cos(angles)
    y = np.sin(angles)

    # Draw the dots
    ax.scatter(x, y, s=50, c='blue')

    # Add dot labels
    for i, (xi, yi) in enumerate(zip(x, y)):
        ax.annotate(str(i+1), (xi, yi), xytext=(3, 3), textcoords='offset points')

    # Draw the arrows
    for i in range(len(connections) - 1):
        a, b = connections[i] - 1, connections[i+1] - 1  # Adjust for 0-based indexing
        arrow = FancyArrowPatch((x[a], y[a]), (x[b], y[b]),
                                arrowstyle='->',
                                color='r',
                                mutation_scale=20)
        ax.add_patch(arrow)

    # Return the figure object
    return fig

'''
This is a program that visualize the circular subgroups of 
    multiplicative modulo groups of size n
It generates the Zn_star first, the set of Ints coprime to n
Then for each unit a of Zn_star, it does a, a^2, a^3 ... until a^k = 1 mod n to generate one cyclic subgroup
Then it draws each sequence out on canvas
'''

def main():
    # Get the number of dots
    n = 42
    Zn_star = generate_multiplicative_group(n)
    circular_subgroups = populate_circular_subgroups(Zn_star)

    for connections in circular_subgroups[1:]:
        draw_dots_and_arrows(n - 1, connections, "Unit " + str(connections[0]))

    plt.show()

if __name__ == "__main__":
    main()