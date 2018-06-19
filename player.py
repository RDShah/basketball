from constants import dt
from ball import Ball
import numpy as np

class player(object):
    def __init__(self, position, velocity, acceleration, **kwargs):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.has_ball = kwargs['has_ball']
        self.history = [(x,y)]
        self.max_velocity = kwargs['max_velocity']
        self.max_acceleration = kwargs['max_acceleration']

    def step(self):
        self.position += dt*self.velocity
        self.velocity += dt*self.acceleration

    def action(self):
        pass

    def get_summary(self):
        return {'position':self.position,'velocity':self.velocity}




