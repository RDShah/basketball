from constants import dt
import numpy as np
from utilz import *

class Ball:
	def __init__(self):
		self.position = np.zeros(2)
		self.acceleration = np.zeros(2)
		self.velocity = np.zeros(2)
		self.is_in_possession = False

	def set_acceleration(self,acc=np.zeros(2)):
		assert self.is_in_possession or (acc==np.zeros(2)).all(),'No one has possession of the ball, it cannot accelerate.'
		self.acceleration = acc

	def step(self):
		self.position += dt*self.velocity
		self.velocity += dt*self.acceleration

		if not in_bounds(self.position):
			self.position = np.zeros(2)
			self.velocity = np.zeros(2)

	def get_summary(self):
		return {'position':self.position,'velocity':self.velocity}