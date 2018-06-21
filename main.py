from constants import dt
from ball import Ball
from player import Player
from utilz import dist
import numpy as np

class Game:
	def __init__(self,players=None,ball=None):
		self.players = players or [Player('home') for _ in range(5)]+[Player('away') for _ in range(5)]# list
		self.ball = ball or Ball()

	def index_of_player_with_possession(self): # right now, possesion is assigned to the player closes to the ball, if that distance is less than 0.5 meters
		distances_from_ball = [dist(player.position,self.ball.position) for player in self.players]
		min_dist = min(distances_from_ball)
		return distances_from_ball.index(min_dist) if min_dist < 0.5 else -1

	def step(self,bad):
		j = self.index_of_player_with_possession()
		if j == -1:
			self.ball.set_acceleration() #default is 0
			self.ball.is_in_possession = False
		else: self.ball.is_in_possession = True
		list_of_summaries = [player.get_summary() for player in self.players] # get summary statistics

		for i in range(len(self.players)):
			self.players[i].action(list_of_summaries[:i]+list_of_summaries[i+1:],self.ball.get_summary(),self.ball if i==j else None) # decide acceleration
			# if i == j:
			# 	self.ball.set_acceleration(self.players[j].set_balls_acceleration(list_of_summaries[:i]+list_of_summaries[i+1:],self.ball.get_summary())) #if has possession, decide balls acceleration
			self.players[i].step() # update posision and velocity
		self.ball.step()

		return [tuple(x['position']) for x in list_of_summaries] + [tuple(self.ball.get_summary()['position'])]
