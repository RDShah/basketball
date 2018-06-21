import matplotlib.pyplot as plt
from matplotlib import animation
import random

import main

fig = plt.figure()
plt.axis('off')
pause = False
iteration = 0

# first five are home team, second five are away team, last is ball
players = [plt.Circle((200 + random.uniform(-50,50), 300 + random.uniform(-50,50)), 10, fc='r') for _ in range(5)]
players_away = [plt.Circle((200 + random.uniform(-50,5 ), 300 + random.uniform(-50,50)), 10, fc='b') for _ in range(5)]
players.extend(players_away)
players.append(plt.Circle((400,400), 10, fc='orange'))

def x_conversion(real_x):
	return 170.0/7*real_x + 340.0

def y_conversion(real_y):
	return -(80.0)/3*real_y + 200.0

def setup_background(background='basketball_court2.png'):
	im = plt.imread(background)
	implot = plt.imshow(im)
	ax = plt.axes()
	for player in players:
		ax.add_patch(player)
	return players,


def onClick(event):
    global pause
    pause ^= True

def animate(i, location_generator):
	global iteration
	curr_location = location_generator(iteration)
	curr_index = 0
	if not pause:
		for player in players:
			player.center = (x_conversion(curr_location[curr_index][0]), y_conversion(curr_location[curr_index][1]))
			curr_index += 1
		iteration += 1
	return players,


def animate_basketball(location_generator):
	global fig
	fig.canvas.mpl_connect('button_press_event', onClick)
	anim = animation.FuncAnimation(fig, animate, 
                               init_func=setup_background, 
                               frames=360, 
                               fargs=(location_generator,),
                               interval=20)
	plt.show()

def test_location_generator(i):
	return [(random.uniform(-14, 14), random.uniform(-7.5, 7.5)) for _ in range(11)]

g = main.Game()

animate_basketball(g.step)

