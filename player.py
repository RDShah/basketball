from constants import dt
from ball import Ball
import numpy as np
from utilz import clip_norm,random_location_on_court,dist
import strategies

class Player(object):
    def __init__(self,i,home_or_away,
        position=None,
        velocity=np.zeros(2),
        acceleration=np.zeros(2),
        **kwargs):

        self.team = home_or_away.lower()
        self.position = position or random_location_on_court()
        self.velocity = velocity
        self.acceleration = acceleration
        #self.history = [(x,y)]
        self.max_velocity = 3#kwargs['max_velocity']
        self.max_acceleration = 100#kwargs['max_acceleration']
        self.passing = False
        self.has_possession = False
        self.index = i

    def step(self):
        self.position += dt*self.velocity
        self.velocity += dt*self.acceleration

        self.velocity = clip_norm(self.velocity,self.max_velocity)

    def action(self,player_summaries,ball_summary,ball): # None is passed if the player doesn't have possession
        self.has_possession = ball is not None
        self.acceleration = 10*strategies.basic_forces2(self,player_summaries,ball_summary,ball)
        self.acceleration = clip_norm(self.acceleration,self.max_acceleration)

    def get_summary(self):
        return {
        'position':self.position,
        'velocity':self.velocity,
        'team':self.team,
        'passing':self.passing,
        'possession':self.has_possession,
        'index':self.index}




