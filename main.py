#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "???"


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    output = 0
    negative = False
    if x < 0:
        x = abs(x)
        negative = not negative
    if y < 0:
        y = abs(y)
        negative = not negative
    for i in range(x):
        output = add(output, y)
    if negative == True:
        output = output - (output + output)
    return output


def power(x, n):
    """Raise x to power n, where n >= 0"""
    output = 1
    for i in range(n):
        output = multiply(output, x)
    return output


def factorial(x):
    """Compute factorial of x, where x > 0"""
    output = 1
    for i in range(1, x+1):
        output = multiply(output, i)
    return output


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    primary = 0
    secondary = 1
    tertiary = 0
    output = 0

    for i in range(n):
        output = add(secondary, primary)
        tertiary = secondary
        secondary = primary
        primary = output
    return output

if __name__ == '__main__':
    # your code to call functions above
    pass
