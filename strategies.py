from utilz import dist,in_bounds,cos_theta,opposite
import random
import numpy as np
from constants import basket

def is_blocking(passer,passee,blocker):
	return cos_theta(
		blocker['position']-passer['position'],
		passee['position']-passer['position'])>0.9

def is_open(passer,passee,player_summaries):
	for blocker in player_summaries:
		if blocker['team']!=passer['team'] and is_blocking(passer,passee,blocker):
			return False
	return True

def can_pass_to(passer,player_summaries):
	li = []
	for passee in player_summaries:
		if passee['team'] == passer['team'] and is_open(passer,passee,player_summaries):
			li.append(passee)
	return li


def basic_forces2(own,player_summaries,ball_summary,ball):
	state = 'get the ball'

	for player in player_summaries + [own.get_summary()]:
		if player['possession'] and player['team'] == own.team:
			state = 'offense'
			break
		elif player['possession']:
			state = 'defense'
	pos = own.position
	point_charges = [
	(np.array([pos[0],7.5]),-5),
	(np.array([pos[0],-7.5]),-5),
	(np.array([14,pos[1]]),-5),
	(np.array([-14,pos[1]]),-5)]

	if state == 'offense':
		#point_charges.append((basket[own.team],10))
		for player in player_summaries:
			point_charges.append((player['position'],-10))
	elif state == 'defense':
		for player in player_summaries:
			if player['index']%5 == own.index%5:
				point = 0.62 * player['position'] + 0.11 * ball_summary['position'] + 0.27 * basket[opposite(own.team)]
				point_charges.append((point,100))
		# 	if player['team'] == own.team:
		# 		point_charges.append((player['position'],-5))
		# 	else:
		# 		point_charges.append((player['position'],1))
	elif state == 'get the ball':
		point_charges.append((ball_summary['position'],100))

	acc = np.zeros(2)
	for point,charge in point_charges:
		acc += charge*(point-pos)/dist(point,pos)**3

	if state == 'offense':
		acc += basket[own.team]-own.position

	if ball is not None and not own.passing:
		li = can_pass_to(own.get_summary(),player_summaries)
		if len(li)>0 and random.random()<0.05:
			print('pass')
			own.passing = True
			own.has_possession = False
			elmt = random.sample(li,1)[0]
			ball.set_acceleration(20*(elmt['position']+0.1*elmt['velocity']-ball_summary['position']))
		else:
			ball.set_acceleration(100*(own.velocity-ball_summary['velocity']))

	return acc


def basic_forces(own,player_summaries,ball_summary,ball):
	own_summary = own.get_summary()
	acc = np.zeros(2)

	if not in_bounds(own_summary['position']):
		return -own_summary['position']

	coef = 4 if np.linalg.norm(ball_summary['velocity'])<7 else 1000
	for summary in player_summaries:
		acc += 4*(-summary['position']+own_summary['position'])/dist(summary['position'],own_summary['position'])**3
	if not own.passing:
		if coef == 4:
			acc += coef*(ball_summary['position']-own_summary['position'])/dist(ball_summary['position'],own_summary['position'])**3
		else:
			target = ball_summary['position'] + (own_summary['position']-ball_summary['position']).dot(ball_summary['velocity'])/np.linalg.norm(ball_summary['velocity'])**2 * ball_summary['velocity']
			acc += coef*(target-own_summary['position'])/dist(target,own_summary['position'])**3

	pos = own_summary['position']
	boundary_points = [np.array([pos[0],7.5]),np.array([pos[0],-7.5]),np.array([14,pos[1]]),np.array([-14,pos[1]])]
	for p in boundary_points:
		acc += 2*(-p+pos)/dist(p,pos)**3

	if ball is None:
		own.passing = False

	if ball is not None and not own.passing:
		li = can_pass_to(own_summary,player_summaries)
		#print('pospas',len(li))
		if len(li)>0 and random.random()<0.05:
			print('pass')
			own.passing = True
			own.has_possession = False
			elmt = random.sample(li,1)[0]
			ball.set_acceleration(20*(elmt['position']+0.1*elmt['velocity']-ball_summary['position']))
		else:
			ball.set_acceleration(100*(own_summary['velocity']-ball_summary['velocity']))

	return acc

