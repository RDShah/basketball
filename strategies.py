from utilz import dist,in_bounds
import random

def is_blocking(passer,passee,blocker):
	return cos_theta(
		blocker['position']-passer['position'],
		passee['position']-passer['position'])
	<0.1

def is_open(passer,passee,player_summaries):
	for blocker in player_summaries:
		if blocker['team']!=passer['team'] and is_blocking(passer,passee,blocker):
			return False
	return True

def can_pass_to(passer,player_summaries):
	li = []
	for passee in player_summaries:
		if passee['team'] == passer['team'] and is_open(passer,passee):
			li.append(passee)
	return li

def basic_forces(own_summary,player_summaries,ball_summary,ball):
	acc = np.zeros(2)

	if not in_bounds(own_summary['position']):
		return -own_summary['position']

	for summary in player_summaries:
		acc += (-summary['position']+own_summary['position'])/dist(summary['position'],own_summary['position'])**3
	acc += 5*(ball_summary['position']-own_summary['position'])/dist(summary['position'],own_summary['position'])**3

	if ball is not None:
		li = can_pass_to(own_summary,player_summaries)
		if len(li)>0 and random.random()<0.005: ball.set_acceleration(li[0]['position']-own_summary['position'])

	return acc

