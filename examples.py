from optimizer import optimize


# Simple example
def ff(x, y):
    return x**2 + y**3 + x*y

def f(vec):
    return ff(*vec)

print optimize(f, [(-4.0, 5.0), (-5.0, 100.0)])

# Measure a time command took running
import time
import subprocess
def gg(logm, logb):
    command = "/home/glapul/studia/ATL/a.out"
    m = 2**logm
    b = 2**logb


