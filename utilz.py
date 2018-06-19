import numpy as np


def clip_norm(vec,mag):
	return vec / max(1,np.linalg.norm(vec)/mag)

def random_location_on_court():
	return np.random.uniform([-14,-7.5],[14,7.5])