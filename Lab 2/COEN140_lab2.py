"""
Name: Ethan Paek
Date: 4/8/2020
Description: COEN 140 Lab #2 - This lab is intended to be get familiar with Python and Jupyter Notebook
by following the steps as written in Lab 2.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
import time

# Step 1
rows = 100
cols = 100

# generate matrices A & B as 10 x 10 matrices
a = np.arange(10000).reshape(rows, cols)
print("Matrix a:\n", a)

b = np.arange(10000).reshape(rows, cols)
print("\nMatrix b:\n", b)


# using 2 for loops to calculate c
def for_loop_add():
    # matrix c will be a + b
    c = np.zeros((rows, cols))
    start_loop_time = time.time() * 1000
    for i in range(rows):
        for j in range(cols):
            c[i][j] = a[i][j] + b[i][j]
    end_loop_time = (time.time() * 1000) - start_loop_time
    return end_loop_time
    # print("\nTime to add by using 2 for loops: ", end_loop_time, "msec")
    # print("\n Matrix C (Matrix A + Matrix B:\n", c)


# we should use milliseconds due to precision rounding
print("\nTime to add by using 2 for loops: ", for_loop_add(), "msec")


# using '+' operator to calculate c
def add_operator_sum():
    c = np.zeros((rows, cols))
    start_operator_time = time.time() * 1000
    c = a + b
    end_operator_time = (time.time() * 1000) - start_operator_time
    return end_operator_time
    # print("\nTime to add by using '+' operator: ", end_operator_time, "msec")
    # print("\n Matrix C (Matrix A + Matrix B:\n", c)


print("\nTime to add by using '+' operator: ", add_operator_sum(), "msec")


# Step 2
def for_loop_vector():
    time_vector = []
    for i in range(0, 10000):
        time_vector.append(for_loop_add())
    print("\n10000 iterations of timing results for adding through for loops:\n", time_vector)
    vector_mean = np.mean(time_vector)
    print("\nAverage of running times: ", vector_mean, "msec")
    vector_std = np.std(time_vector)
    print("Standard deviation of running times: ", vector_std, "msec")
    plt.hist(time_vector)
    plt.xlabel('Time taken to execute (ms)')
    plt.ylabel('Number of time trials')
    plt.title("Times when adding matrices with 2 for loops")
    plt.show()


for_loop_vector()


def add_operator_vector():
    time_vector = []
    for i in range(0, 10000):
        time_vector.append(add_operator_sum())
    print("\n10000 iterations of timing results for adding through '+' operator:\n", time_vector)
    vector_mean = np.mean(time_vector)
    print("\nAverage of running times: ", vector_mean, "msec")
    vector_std = np.std(time_vector)
    print("Standard deviation of running times: ", vector_std, "msec\n")
    plt.hist(time_vector)
    plt.xlabel('Time taken to execute (ms)')
    plt.ylabel('Number of time trials')
    plt.title("Times when adding matrices with '+' operator")
    plt.show()


add_operator_vector()
