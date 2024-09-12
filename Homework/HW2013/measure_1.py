import numpy as np
from scipy.optimize import curve_fit
from scipy.optimize import bisect
from scipy.interpolate import interp1d
from scipy.misc import derivative
from scipy.integrate import odeint
import const
import final
#import reference as rfr
from pylab import * # for plotting commands
import time
import scoring

TNUM = 1000;
def field1(y, g):
	arr = np.empty(len(y))
	arr[:] = g
	return arr

def field2(y, r, n):
	return -const.G * (r + y)**(-n)

def xpath(t, b, v0):
	return - v0 / b * np.exp(-b * t) + v0 / b

def measure(data):
	xs = data[0]
	ys = data[1]
	check = list(abs(np.diff(xs)) > 1E-6)
	if all(check):
		return True, xs, ys
	else:
		idx = check.index(False)
		return False, xs[idx], ys[idx]


def sampling(vel, ang, ticks, times):
	ret = measure(final.track(vel, ang, ticks))
	if ret[0]:
		sum_xs, sum_ys = ret[1], ret[2]
	else:
		return False
	for t in range(times-1):
		xs, ys = final.track(vel, ang, ticks)
		sum_xs += xs
		sum_ys += ys
	ave_xs = sum_xs / times
	ave_ys = sum_ys / times

	return ave_xs, ave_ys


def processing(xs, ys, vx0, ticks, deg, func, vel, ang):
	popt, pcov = curve_fit(xpath, ticks, xs, [0.1, vx0])
	b = popt[0]
	#-------------------------------
	#ypara = np.polyfit(ticks, ys, deg)
	#yt = np.poly1d(ypara)
	#-------------------------------
	ang = ang / 180.0 * np.pi
	def yfit(t,r,n):
		def yderi(Y,t):
			return np.array([Y[1], field2(Y[0],r,n) - Y[1] * b])
		Y0 = np.array([0.0, vel * np.sin(ang)])
		Y = odeint(yderi, Y0, t)
		return Y[:,0]
	"""
	plot(xs, ys)
	plot(xs, yt(ticks))
	plot(xs, yt(ticks))
	show()
	"""
	#-------------------------------
	#dt = ticks[1] - ticks[0]
	#vyt = derivative(yt, ticks, dx=dt, n=1)
	#ayt = derivative(yt, ticks, dx=dt, n=2)
	#fy = ayt + b * vyt
	#-------------------------------
	"""
	plot(ys, fy)
	show()
	"""
	popt,pcov=curve_fit(yfit,ticks,ys,[300.0,2.00])
	print "AAAAAAAAAAAAAAAAA",popt
	#-------------------------------
	#popt, pcov = curve_fit(func, ys[50:-50], fy[50:-50], [300.0, 2.0])
	#popt, pcov = curve_fit(func, ys[50:-50], fy[50:-50], [10])
	#-------------------------------
	return popt,b

def derive(Y, t, b, r, n): #Y[0] = x, Y[1] = x', Y[2] = y, Y[3] = y'
	return np.array([Y[1], -Y[1] *  b, Y[3], field2(Y[2],r,n) - Y[3] * b]);

def track(vel, ang, slices, xbar, ybar1, ybar2, b, r, n):
	'''
	vel: velocity(m/s)
	ang: angle(degree)
	slices: time slices, numpy array.
	'''
	slices = np.array(slices)
	ang = ang / 180.0 * np.pi
	Y0 = np.array([0.0, vel * np.cos(ang), 0.0, vel * np.sin(ang)])
	try:
		Y = odeint(lambda Y,t: derive(Y,t,b,r,n), Y0, slices)
	except:
		return False,False
	xs = np.array(Y[:,0])
	ys = np.array(Y[:,2])
	xline=np.linspace(0,110,1001)
	yline=np.zeros(1001)
	"""
	plot(xs,ys,xline,yline)
	plot(xbar,ybar1,'o',xbar,ybar2,'o')
	show()
	"""

	try:
		traj = interp1d(xs, ys)
		height = traj(xbar)
		if height < ybar1 or height > ybar2:
#			idx = bsearch(xs, barx, 0, len(xs))
			try:
#				xs[idx+1:] = barx
#				ys[idx+1:] = 0.0
				return False,xs, ys
			except:
				pass
	except:
		pass
	return True, xs , ys

def find_vel(xbar,ybar1,ybar2,b,R,n,vel,ang,x):
	vel_up, vel_low = 3.0*vel, 0.0
	ybarmean=(ybar1+ybar2)/2
	while(1):
		rad = ang / 180.0 * np.pi
		vx=vel*cos(rad)
		t=x/vx*0.7
		ticks=np.arange(0.0,t,0.001)
		"""
		print "vel=", vel,"ang=", ang
		"""
		while(1):
			ret=track(vel, ang, ticks, xbar, ybar1, ybar2, b, R, n)

			#plot(ret[1],ret[2])
			#show()
			if(ret[1][-1]>x):
				break
			elif (ret[2][-2]-ret[2][-1]>0.12):
				print "====================="
				return False,-2.0,0.0
			else :
				t += x/vx*0.03
				ticks=np.arange(0.0,t,0.001)

		#print vel_up,vel_low
		traj = interp1d(ret[1], ret[2])
		if abs(traj(x))<0.005:
			if ret[0]==True:
				xline=np.linspace(0, x, 1001)
				yline=np.zeros(1001)
				"""
				plot(ret[1],traj(ret[1]))
				plot(xline,yline)
				plot(xbar,ybar1,'o',xbar,ybar2,'o')

				show()
				"""
				trajty=interp1d(ticks,ret[2])
				return ret[0],vel,bisect(trajty,0.1,ticks[-1])

			else:
				xline=np.linspace(0, x, 1001)
				yline=np.zeros(1001)
				"""
				plot(ret[1],traj(ret[1]))
				plot(xline,yline)
				plot(xbar,ybar1,'o',xbar,ybar2,'o')

				show()
				"""
				#plot(ret[1],traj(ret[1]))
				#show()
				#================================================correct the angle==============================================
				delta_ang = (np.arctan(ybarmean/xbar)-np.arctan(traj(xbar)/xbar))/(ybarmean/xbar/np.arctan(ybarmean/xbar)+traj(xbar)/xbar/np.arctan(traj(xbar)/xbar))*180.0/np.pi
				if delta_ang>0:
					delta_ang=max(4.0,delta_ang)
				else:
					delta_ang=min(-4.0,delta_ang)
				#print "!!!!!!!!!",delta_ang
				return ret[0],delta_ang,0.0
		elif traj(x)>0 :
			vel_up=vel
			vel=(vel+vel_low)/2
		elif traj(x)<0 :
			vel_low=vel
			vel=(vel+vel_up)/2



def aiming(x, xbar, ybar1, ybar2, b, R, n):
	ang=45.0
	ang_up, ang_low = 200.0, -200.0
	while(1):
		rad = ang / 180.0 * np.pi
		vx = np.sqrt(rfr.g*x/2.0/np.tan(rad))
		t=x*2/vx
		vel=vx/np.cos(rad)
		n_pass,vel,T = find_vel(xbar,ybar1,ybar2,b,R,n,vel,ang,x)
		if n_pass==True:
			print "final ang=",ang,
			print "final vel=",vel
			#"""""""""""""""""""""""""""determine the ticks""""""""""""""""""""""""""""
			return vel , ang, linspace(0.0,T,TNUM)
		elif n_pass==False:
			print "!!!!!!!!",ang_up,ang_low
			if ang_up<90.0 and ang_low>-90.0:
				if vel>0:
					ang_low = ang
				else:
					ang_up = ang
				ang = (ang_up+ang_low)/2.0
			else:
				if vel>0:
					ang_low = ang
				else:
					ang_up = ang
				if ang_up<90.0 and ang_low>0.0:
					ang = (ang_up+ang_low)/2.0
				else:
					ang=ang+vel









def adjustV(ang, Vpass, Vfail, Verr, ticks):
	if abs(Vpass - Vfail) < Verr:
		ret = measure(final.track(Vpass, ang, Tticks))
		if ret[0]:
			return Vpass
	vel = (Vpass + Vfail) / 2
	ret = measure(final.track(vel, ang, Tticks))
	if ret[0]:
		adjustV(ang, vel, Vfail, Verr, ticks);
	else:
		adjustV(ang, Vpass, vel, Verr, ticks);

def adjustT(vel, ang, ticks):
	ret = measure(final.track(vel, ang, ticks))
	ys = ret[2]
	if ys[-1] > -1:
		ticks = np.linspace(ticks[0], 1.1 * ticks[-1], TNUM)
		return adjustT(vel, ang, ticks)
	cnt = 0
	for y in reversed(ys):
		if y > -1:
			return ticks[-cnt]
		cnt += 1

def adjustA(vel, Amin, Amax, div_num):
	angs = np.linspace(Amin, Amax, div_num)
	for ang in angs:
		Tmax = estimateT(ang, vel)
		ticks = np.linspace(0.0, Tmax, TNUM)
		ret = measure(final.track(vel, ang, ticks))
		if ret[0]:
			Amin = ang;
			break
	for ang in reversed(angs):
		Tmax = estimateT(ang, vel)
		ticks = np.linspace(0.0, Tmax, TNUM)
		ret = measure(final.track(vel, ang, ticks))
		if ret[0]:
			Amax = ang;
			break
	return Amin, Amax

def funcT(vel, ang, tarX):
	rad = ang / 180.0 * np.pi
	return (-1.0 / rfr.b) * np.log(1 - rfr.b * tarX / (vel * np.cos(rad)))

def estimateV(ang, tarX):
	rad = ang / 180.0 * np.pi
	return np.sqrt(float(rfr.g) * 1.6 * tarX / sin(2 * rad))

def estimateT(ang, vel):
	rad = ang / 180.0 * np.pi
	return 2.0 * vel * np.sin(rad) / rfr.g

def find_bar(vel,esamax,esamin):
	ang=esamax
	xbars=[]
	while(1):
		ticks = np.linspace(0.0, 50.0, TNUM)
		ret = measure(final.track(vel, ang, ticks))
		if ret[0]:
			Amin = ang;
			break
		else :
			xbars.append(ret[1])
		ang-=0.1
	ang=esamin
	while(1):
		ticks = np.linspace(0.0, 50.0, TNUM)
		ret = measure(final.track(vel, ang, ticks))
		if ret[0]:
			Amax = ang;
			break
		else :
			xbars.append(ret[1])
		ang+=0.1
	xbar=np.array(xbars).mean()
	#print Amax,Amin
	rad=Amax/ 180.0 * np.pi
	ybar1=xbar*np.tan(rad)
	rad=Amin/ 180.0 * np.pi
	ybar2=xbar*np.tan(rad)
	return xbar,ybar1,ybar2




def controller(func=field2, num=4000, distance=100):
	ang = 45
	vel = estimateV(ang, rfr.Xmax)
	rad = ang / 180.0 * np.pi

	#decide ang
	Amin, Amax = adjustA(vel, 10, 80, 101)
	ang = (Amin + Amax) / 2

	#decide ticks
	Tmax = estimateT(ang, vel)
	ticks = np.linspace(0.0, Tmax, TNUM)
	Tmax = adjustT(vel, ang, ticks)
	print "Tmax", Tmax
	#print vel, ang, Tmax
	ticks = np.linspace(0.0, Tmax, TNUM)
	start = time.clock()
	ret = sampling(vel, ang, ticks, num)
	end = time.clock()
	xbar,ybar1,ybar2 = find_bar(6000,Amax,18.0)
	ybar1=ybar1+0.3 # for safety
	ybar2=ybar2-0.3
	print xbar,ybar1,ybar2
	if ret:
		xs, ys = ret
		Rn,b=processing(xs, ys, vel * np.cos(rad), ticks, 8, func, vel, ang)
		R,n=Rn
		return R,n
		print "R:", R,"n:", n,"b:", b
		vel,angle, outTicks= aiming(distance,xbar,ybar1,ybar2,b,R,n)
		return vel,angle, outTicks


