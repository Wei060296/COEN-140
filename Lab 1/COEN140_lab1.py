"""
Name: Ethan Paek
Date: 4/1/2020
Description: COEN 140 Lab #1 - This lab is intended to be a Python introduction (or brush-up)
by following the steps as written in Lab 1.pdf
"""

import csv
import operator
from operator import itemgetter
import emojis


# Requirement 1
def odd_list(n):
    nums = []
    for i in range(1, n + 1, 2):  # range(start, stop, step)
        nums.append(i)
    return nums


print(odd_list(10))


# Requirement 2
def read_csv():
    with open("students.csv", 'r') as file:
        data = [line for line in csv.reader(file)]

    # for part a
    alphabetically = data
    alphabetically.sort(key=itemgetter(0))
    print(alphabetically)

    # for part b
    data.sort(key=itemgetter(1))
    print(data)


read_csv()


# Requirement 3
def count_chars(inputstr):
    dictvals = {}
    for i in inputstr:
        keys = dictvals.keys()
        if i in keys:
            dictvals[i] += 1
        else:
            dictvals[i] = 1
    print(dictvals)
    maxval = max(dictvals.items(), key=operator.itemgetter(1))[0]
    return "Most frequent character in your string is: " + maxval


print(count_chars("google.com"))


# Requirement 4
def amazing_emojis():
    emojified = emojis.encode("There's a :snake: in my boot!")
    print(emojified)


amazing_emojis()
