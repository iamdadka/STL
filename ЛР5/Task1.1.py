import numpy as np
x = 0.3
a = 756.13
print(np.cos(x ** 2 + np.pi / 6) ** 5
    - (x * a ** 3) ** 0.5
    - np.log(np.abs((a - 1.12 * x) / 4)))
