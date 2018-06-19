import numpy as np

def in_bounds(x):
	return abs(x[0]) <= 14 and abs(x[1]) <= 7.5

def dist(a,b):
	return np.linalg.norm(a-b)

def clip_norm(vec,mag):
	return vec / max(1,np.linalg.norm(vec)/mag)

def random_location_on_court():
	return np.random.uniform([-14,-7.5],[14,7.5])
