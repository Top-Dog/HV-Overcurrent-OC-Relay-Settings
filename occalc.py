# Author: SDO
# Date: 28/09/2019
# Description: Calculate the best fit TMS and PU setting
# from two test points on the standard overcurrent curve
# as defined by equation f (below).

from sympy import * # symbol, nsolve

################## User Supplied Parameters ##################
CTRatio = 400/1
point1 = Point(0.7*CTRatio, 1.923)      # Test point one (x,y)
point2 = Point(3.5*CTRatio, 0.219)      # Test point two (x,y)
curve = Curve("IEC very inverse Class B")
hint = [0.2, 0.1]       # The approximate [PU, TMS] settings
##############################################################

class Point():
	def __init__(self, x, y):
		"""The point (X, Y) reprsents (Current, Trip Time).
		Usually the standard test currents are 0.7 A * CTR and 2.45 A * CTR"""
		self.x = x
		self.y = y
		
class Curve():
	def __init__(self, name):
		if name == "IEC standard inverse Class A":		# IEC C1
			self.X = 0.14
			self.P = 0.02
			self.Y = 0
		elif name == "IEC very inverse Class B":		# IEC C2
			self.X = 13.5
			self.P = 1
			self.Y = 0
		elif name == "IEC extremely inverse Class C":	        # IEC C3
			self.X = 80
			self.P = 2
			self.Y = 0
		elif name == "IEC long-time inverse":
			self.X = 120
			self.P = 1
			self.Y = 0
		elif name == "IEC short-time Inverse":
			self.X = 0.05
			self.P = 0.04
			self.Y = 0
		elif name == "US Moderately Inverse":
			self.X = 0.0104
			self.P = 0.02
			self.Y = 0.0226
		elif name == "US Inverse":
			self.X = 3.95
			self.P = 2
			self.Y = 0.18
		elif name == "US Very Inverse":
			self.X = 3.88
			self.P = 2
			self.Y = 0.0963
		elif name == "US Extremely Inverse":
			self.X = 5.67
			self.P = 2
			self.Y = 0.0352
		elif name == "US Short-time Inverse":
			self.X = 0.00342
			self.P = 0.02
			self.Y = 0.00262
		else:
			raise Exception("Could not reconsile the supplied curve name: '{0}'".format(name))

# Define Variables
X = Symbol('X')
P = Symbol('P')
Y = Symbol('Y')
TMS = Symbol('TMS')
I = Symbol('I')
t = Symbol('t')
CTR = Symbol('CTR')
PU = Symbol('PU')

# Define Equation (= 0)
f = TMS * (Y + X / ((I / (CTR * PU)) ** P - 1)) - t
g = f.subs({X: curve.X, P: curve.P, Y: curve.Y, CTR: CTRatio, I: point1.x, t: point1.y})
h = f.subs({X: curve.X, P: curve.P, Y: curve.Y, CTR: CTRatio, I: point2.x, t: point2.y})

# Ex. PU is 1.4, TMS is 0.2
try:
	Pickup, Timemultiplier = nsolve([g, h], [PU, TMS], hint)
	print ("The pickup (PU): %.2f\nThe time multiplier setting (TMS): %.2f" % ( Pickup, Timemultiplier))
except ValueError as err:
	print (err)
