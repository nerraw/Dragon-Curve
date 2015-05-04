# Dragon Curve Plot
# 4 May 2015 (Happy Star Wars Day!)
# by Warren Brodsky 
#
#
#
#
#
# The Dragon Curve is created by continuously folding a paper in half
# and then unfolding it partially so each crease is a right angle
# either turning left or right. 
#
# There is a recursive element to the construction of the curve (although I
# have implemented it here with for loops). The idea is that if the paper was folded
# infinite times, every iteration, you're just unfolding a layer. The current iteration
# is two layers. The top layer becomes reversed, inverted, and rotated 90 degrees as 
# part of the unfolding process. The second layer however, remains exactly as is. 
# Therefore every iteration is the previous iteration, preceded by the 90 degree turn, 
# and then preceded by the previous iteration reversed and inverted. 



import numpy as np
import matplotlib.pyplot as plt

# Generate a string of which direction to turn (i.e. L for left and R for right)

curve = "L"								# A "base case" 


for x in range(13):						# 13 iterations. You can choose whatever n you
										# wish but be advised that the Dragon Curve is
										# of order 2^n
										
	temp = ""									
	for i in curve:						# Invert the current iteration
		if i == "L":
			temp = temp + "R"
		else:
			temp = temp + "L"
	temp = temp[::-1] + "L" + curve		# Concatenate the reverse if the inverse with the
	curve = temp						# 90 degree turn and the current iteration



# Convert the directions to geometric movements
x = [0]								# The lists of movements we make in the horizontal			
y = [1]								# and vertical directions, respectively					


# In this for loop, we iterate through every direction in the list we just generated. 
# The initial command counts by two, but i is incremented halfway through. This is 
# because after each 90 degree turn, we alternate whether we are moving in the x direction
# or the y direction.

for i in range(0,len(curve),2):	
	
	if curve[i] == "R":				# If we just moved up, a right turn is in the positive
		x = x + [y[i]]				# x direction, and if we moved down, right is in the					
	else:							# negative direction. I.e. a right turn is toward
		x = x + [-1*y[i]]			# the same extreme as the extreme we just moved toward
	y = y + [0]						# in the vertical direction. The reverse is true for
	i = i+1							# a left turn in the horizontal direction or a right
	if i>=len(curve):				# turn in the vertical direction. And a left turn in
		break						# the vertical direction moves similarly to a right
	if curve[i] == "L":				# turn in the horizontal direction.
		y = y + [x[i]]
	else:
		y = y + [-1*x[i]]
	x = x + [0]


# Plot our course
X = [0]								# The lists of coordinates, starting at the origin
Y = [0]

a = 0								# Our current position (a,b)
b = 0


for i,j in zip(x,y):				# i iterates through x and j iterates through y
	a = a+i							# a moves according to x
	b = b+j							# b moves according to y
	X = X + [a]						# Add our new position to the list
	Y = Y + [b]

# Plot
line, = plt.plot(X, Y, linewidth=.5)
plt.axis('equal')
plt.show()
