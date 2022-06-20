# Predator-Prey Model
# Description: Simulation that uses the Lotka-Volterra equations to solve for the prey
# and predator relationship between lynxes and snowshoe hares using Euler method.

import numpy as npy
import matplotlib.pyplot as plt
import random

# variables for simulation
time_step = 0.001  # determine accuracy of Euler method
amplitude = 0.01
sim_end_time = 100

time = npy.arange(0, sim_end_time, time_step)
x_plot = []  # hares
y_plot = []  # lynxes


def noise(amp):
    """Returns noise to influence differential equation"""
    return amp * random.uniform(-1, 1)


# Lotka-Volterra parameters
alpha = 1  # birth rate of hares
beta = 0.1  # death rate of hares by predation
gamma = 0.5  # natural death rate of lynxes
delta = 0.02  # new lynxes born from consumption of hares

x_plot.append(100)  # at time = 0
y_plot.append(20)

# euler integration
for index in range(1, len(time)):
    # evaluate current differentials
    alpha = alpha + noise(amplitude)  # effect om birth rate
    x_diff = x_plot[index - 1] * (alpha - beta * y_plot[index - 1])
    y_diff = -y_plot[index - 1] * (gamma - delta * x_plot[index - 1])

    # evaluate the next value of x and y with differentials and add noise
    next_x = x_plot[index - 1] + x_diff * time_step
    next_y = y_plot[index - 1] + y_diff * time_step

    x_plot.append(next_x)
    y_plot.append(next_y)

# graphing the model
if amplitude == 0.01:
    # population vs time
    plt.plot(time, x_plot)
    plt.plot(time, y_plot)
    plt.xlabel('Time')
    plt.ylabel('Population Size')
    plt.legend(('Hares', 'Lynxes'))
    plt.title('Lotka-Volterra Model')
    plt.show()

    # phase-space plot
    plt.plot(x_plot, y_plot)
    plt.xlabel('Lynx Population')
    plt.ylabel('Hare Population')
    plt.title('Phase-space plot of Lotka-Volterra')
    plt.show()
