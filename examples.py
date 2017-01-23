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
def gg(m, b):
    m = int(m)
    b = int(b)   
    command = "/home/glapul/studia/ATL/script.fish"
    print "started"
    otp = subprocess.check_output(["fish", command, str(m), str(b)])
    print "finished"
    return float(otp)

def g(v):
    return gg(*v)

print optimize(g, [(5*10**4, 10**6), (10**4, 2*10**5)])




