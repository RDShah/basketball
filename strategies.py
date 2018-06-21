from utilz import dist,in_bounds,cos_theta
import random
import numpy as np

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

def basic_forces(own,player_summaries,ball_summary,ball):
	own_summary = own.get_summary()
	acc = np.zeros(2)

	if not in_bounds(own_summary['position']):
		return -own_summary['position']

	for summary in player_summaries:
		acc += 4*(-summary['position']+own_summary['position'])/dist(summary['position'],own_summary['position'])**3
	if not own.passing:
		acc += 4*(ball_summary['position']-own_summary['position'])/dist(ball_summary['position'],own_summary['position'])**3

	pos = own_summary['position']
	boundary_points = [np.array([pos[0],7.5]),np.array([pos[0],-7.5]),np.array([14,pos[1]]),np.array([-14,pos[1]])]
	for p in boundary_points:
		acc += 2*(-p+pos)/dist(p,pos)**3

	if ball is None:
		own.passing = False

	if ball is not None and not own.passing:
		li = can_pass_to(own_summary,player_summaries)
		#print('pospas',len(li))
		if len(li)>0 and random.random()<0.005:
			print('pass')
			own.passing = True
			elmt = random.sample(li,1)[0]
			ball.set_acceleration(10*(elmt['position']-ball_summary['position']))
		else:
			ball.set_acceleration(100*(own_summary['velocity']-ball_summary['velocity']))

	return acc

