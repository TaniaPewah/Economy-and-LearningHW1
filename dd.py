import numpy as np

x2 = 100
mu, sigma = x2, 45  # Mean and SD
sample_number = np.random.normal(mu, sigma, 1)
print(sample_number)