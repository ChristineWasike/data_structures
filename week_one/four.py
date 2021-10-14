import matplotlib.pyplot as plt
import numpy as np
from week_one.functions import *
from week_one.one import *
from week_one.two import *
from random import random, choice
from string import ascii_uppercase
import string


# TIME PLOTS

def plot_func(function, plot_title, y_axis_label):
    input_x_axis = []
    time_y_axis = []

    for number in range(1, 101, 10):
        input_x_axis.append(number)
        time_y_axis.append(max_value_time_tracker(number))
        function(number)

    print(input_x_axis)
    print(time_y_axis)
    plt.title(plot_title)
    plt.xlabel("Input ranging from 1 to 100")
    plt.ylabel(y_axis_label)
    plt.plot(input_x_axis, time_y_axis)
    plt.show()


time_y_plot = "Time in seconds"
memory_y_plot = "Memory in ..."


def max_value_time_plot():
    plot_func(max_value_time_tracker, "Max value Algorithm Time Tracker", time_y_plot)


def lower_case_time_plot():
    input_x_axis = []
    time_y_axis = []
    for i in range(1, 101, 10):
        input_x_axis.append(i)
        time_y_axis.append(lower_case_time_tracker(''.join(choice(ascii_uppercase) for i in range(i))))
    plt.title("Lowercase time tracker")
    plt.xlabel("Input ranging from 1 to 100")
    plt.ylabel("Lowercase algorithm time tracker")
    plt.plot(input_x_axis, time_y_axis)
    plt.show()


def list_sort_time_plot():
    plot_func(list_sort_time_tracker, "List sorting Algorithm Time Tracker", time_y_plot)


# Here is where I am calling the functions that plot the graphs of time taken for
# the different algorithms against varied input

# max_value_time_plot()
# lower_case_time_plot()
# list_sort_time_plot()


# SPACE PLOTS

def max_value_space_plot():
    plot_func(max_value_memory, "Max value Algorithm Memory Tracker", memory_y_plot)


max_value_space_plot()

# Create a for loop with a range of 1 - 101 for the first and third algorithm.
# Create intervals of 10 to serve as the different inputs for the graph
# Lastly, plot the graph using Matplotlib
