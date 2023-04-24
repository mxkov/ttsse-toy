import numpy as np

def norm_array(n=10, mean=0.0, std=1.0, randomstate=42):
	np.random_seed(randomstate)
	return np.random.normal(loc=mean, scale=std, size=n)
