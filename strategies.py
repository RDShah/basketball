from utilz import dist,in_bounds

def basic_forces(own_summary,player_summaries,ball_summary):
	acc = np.zeros(2)

	if not in_bounds(own_summary['position']):
		return -own_summary['position']

	for summary in player_summaries:
		acc += (-summary['position']+own_summary['position'])/dist(summary['position'],own_summary['position'])**3
	acc += 5*(ball_summary['position']-own_summary['position'])/dist(summary['position'],own_summary['position'])**3
	return acc

