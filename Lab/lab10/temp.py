import final
import numpy as np
from scipy.optimize import curve_fit
#f=open('data_lab10.dat','w')
ts=np.linspace(0,1,101)

v0=15
ang=45
xs, ys = final.track(v0,ang,ts)
vx0=v0*np.cos(ang/180.*np.pi)
vy0=v0*np.sin(ang/180.*np.pi)

xs=xs[:-2]
ys=ys[:-2]
ts=ts[:-2]
#for i in range(len(ts)):
#        print >> f, ts[i], xs[i], ys[i]
#f.close()
def fx(t, b):
	return -vx0/b*np.exp(-t*b)+vx0/b
#for b in np.linspace(0.9, 0.11):
#	bts = b*ts
#	popt, pcov =  curve_fit(fx, bts, xs)
bb, = curve_fit(fx, ts, xs, p0=[.1])[0]
print bb
def fy(t, g):
	return -(vy0+g/bb)/bb*np.exp(-bb*t) + (vy0+g/bb)/bb - g/bb*t

print curve_fit(fy, ts, ys, p0=[10.])[0][0]
