import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d
import _para
from pylab import * # for plotting commands

def derive(Y, t): #Y[0] = x, Y[1] = x', Y[2] = y, Y[3] = y'
	return np.array([Y[1], -Y[1] *  _para.b, Y[3], _para.field(Y[2]) - Y[3] * _para.b]);

def track(vel, ang, slices):
	'''
	vel: velocity(m/s)
	ang: angle(degree)
	slices: time slices, numpy array.
	'''
	slices = np.array(slices)
	ang = ang / 180.0 * np.pi
	Y0 = np.array([0.0, vel * np.cos(ang), 0.0, vel * np.sin(ang)])
	Y = odeint(derive, Y0, slices)
	xs = np.array(Y[:,0])
	ys = np.array(Y[:,2])
	#try:
	if True:
		traj = interp1d(xs, ys)
		print _para.barX
		height = traj(_para.barX)
		if height < _para.barY1 or height > _para.barY2:
			idx = bsearch(xs, _para.barX, 0, len(xs))
			#try:
			if True:
				xs[:idx + 1] + _para.noise * np.random.normal(size=(idx + 1))
				ys[:idx + 1] + _para.noise * np.random.normal(size=(idx + 1))
				xs[idx+1:] = _para.barX
				ys[idx+1:] = 0.0
				return xs, ys
			#except:
			else:
				pass
	#except:
	else:
		pass
	return xs + _para.noise * np.random.normal(size=len(slices)), ys + _para.noise * np.random.normal(size=len(slices))

def bsearch(xs, barX, left, right):
	mid = (left + right) / 2
	if right - left <= 1:
		return mid;
	if xs[mid] <= barX:
		return bsearch(xs, barX, mid, right)
	else:
		return bsearch(xs, barX, left, mid)
