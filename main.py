from constants import dt
from ball import Ball

class Game:
	def __init__(self,players,ball):
		self.players = players # list
		self.ball = ball or Ball()

	def index_of_player_with_possession(self): # right now, possesion is assigned to the player closes to the ball
		distances_from_ball = [np.linalg.norm(player.position - ball.position) for player in self.players]
		return distances_from_ball.index(min(distances_from_ball))

	def step():
		j = self.index_of_player_with_possession()

		list_of_summaries = [player.get_summary() for player in self.players] # get summary statistics

		for i in range(len(self.players)):
			players[i].make_move(list_of_summaries[:i]+list_of_summaries[i+1:]) # decide acceleration
			if i == j: self.ball.set_acceleration(players[j].set_balls_acceleration(list_of_summaries[:i]+list_of_summaries[i+1:])) #if has possession, decide balls acceleration
			players[i].step() # update posision and velocity

