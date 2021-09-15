#%%

import math
k = 0
c = 0
while abs(1/math.pi-c) >= 1e-15:
    a = ((math.factorial(4*k))*(1103+26390*k)) / ((math.factorial(k)**4)*(396**(4*k)))
    b = (2*math.sqrt(2)/9801)*a
    c = b+c
    k = k+1
print("%.20f" % (1/math.pi-c))