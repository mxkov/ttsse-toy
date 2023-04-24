import numpy as np
import matplotlib.pyplot as plt

def norm_array(n=10, mean=0.0, std=1.0, randomstate=42):
	np.random.seed(randomstate)
	return np.random.normal(loc=mean, scale=std, size=n)

def plot_hist(x, filename='hist.png'):
	plt.hist(x, bins='auto')
	plt.savefig(filename, dpi=200, bbox_inches='tight')
	plt.close()

if __name__ == '__main__':
	plot_hist(norm_array(n=20), filename='hist20.png')
