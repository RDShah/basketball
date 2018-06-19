from constants import dt
from ball import Ball
import numpy as np
from utilz import clip_norm,random_location_on_court
import strategies

class Player(object):
    def __init__(self,home_or_away,
        position,
        velocity=np.zeros(2),
        acceleration=np.zeros(2),
        **kwargs):
        self.home = home_or_away.lower() == 'home'
        self.position = position or random_location_on_court()
        self.velocity = velocity
        self.acceleration = acceleration
        self.history = [(x,y)]
        self.max_velocity = kwargs['max_velocity']
        self.max_acceleration = kwargs['max_acceleration']

    def step(self):
        self.position += dt*self.velocity
        self.velocity += dt*self.acceleration

        self.velocity = clip_norm(self.velocity,self.max_velocity)

    def action(self,player_summaries,ball_summary,ball): # None is passed if the player doesn't have possession
        self.acceleration = strategies.basic_forces(self.get_summary(),player_summaries,ball_summary,ball)
        self.acceleration = clip_norm(self.acceleration,self.max_acceleration)

    def get_summary(self):
        return {'position':self.position,'velocity':self.velocity,'team':self.home}




