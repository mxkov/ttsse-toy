import numpy as np
import matplotlib.pyplot as plt

def norm_array(n=10, mean=0.0, std=1.0, randomstate=42):
	return np.random.normal(loc=mean, scale=std, size=n)

def plot_hist(x):
	raise NotImplementedError
