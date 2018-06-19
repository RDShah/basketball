from constants import dt
from ball import Ball
from player import Player

class Game:
	def __init__(self,players,ball):
		self.players = players or [Player('home') for _ in range(5)]+[Player('away') for _ in range(5)]# list
		self.ball = ball or Ball()

	def index_of_player_with_possession(self): # right now, possesion is assigned to the player closes to the ball, if that distance is less than 0.5 meters
		distances_from_ball = [dist(player.position,ball.position) for player in self.players]
		min_dist = min(distances_from_ball)
		return distances_from_ball.index(min_dist) if min_dist < 0.5 else -1

	def step():
		j = self.index_of_player_with_possession()

		list_of_summaries = [player.get_summary() for player in self.players] # get summary statistics

		for i in range(len(self.players)):
			players[i].action(list_of_summaries[:i]+list_of_summaries[i+1:],self.ball.get_summary(),self.ball if i==j else None) # decide acceleration
			if i == j:
				self.ball.set_acceleration(players[j].set_balls_acceleration(list_of_summaries[:i]+list_of_summaries[i+1:],self.ball.get_summary())) #if has possession, decide balls acceleration
			players[i].step() # update posision and velocity