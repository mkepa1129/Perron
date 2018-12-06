import numpy as np
import matplotlib.pyplot as plt

def square(t):
	temp = t**2
	return temp

t0 = 0
T = 100.0
Nt = 2**10 +1
	
t = np.linspace(t0, T, Nt)

plt.plot(t, square(t), 'o')

plt.xlabel("Value of t")
plt.ylabel("Value of f(t)")
plt.title("f(t) = t**2")
plt.legend()
plt.show