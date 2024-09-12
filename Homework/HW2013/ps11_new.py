



import sys,random
from spacecraft import *
random.seed()
class Missile(object):
    """ A missile """
    velo_y=10
    def __init__(self, x=0., y=0.):
        """ Initialize parameters """
        self.x=x
        self.y=y
        self.fired=False
        
    def update(self,dt):
        """ Update the position of the missile"""
        if self.fired :
            self.y=self.y+self.velo_y*dt

    def firing(self):
        """ Fire the missile"""
        if self.fired==False:
            self.fired=True
        else:
            print "Missile is already on the way!"
    def get_position(self):
        return (self.x,self.y)
        
class Base(object):
    """ A base which processes the trajectory data and approximate it with
        a polynomial of degrees n.
    """
    
    def __init__(self, x=0.,y=0.):
        """ Initialize parameters """
        self.x=x
        self.y=y
        self.trajectory=[]
        
        
    def add_traj_data(self, data):
        """ Add the current object position to the trajectory,
            data is a tuple  (obj_x,obj_y) of the current position of the
            moving object"""
        self.trajectory.append(data)
    
    def approx_traj(self,n):
        """ Fit the trajectory data with polynomial of degree n """
        pass 

    def intercept(self, missile):
        """ compute the firing time of a missile"""
        pass
def physics(t):
    # Model the trajectory of the ship as x=4t, y=100+3t-5t^2.

    x0=0.
    y0=100.
    vx_0=4.
    vy_0=3.
    ax=0.
    ay=-10.
    x=  x0+vx_0*t+random.gauss(0,0.1)
    y=  y0+vy_0*t+0.5*ay*t**2+random.gauss(0,0.1)
    vx= vx_0+ax*t
    vy= vy_0+ay*t
    return (x, y, vx,vy)
    
def main():
    missile1=Missile(100,0)
    base1=Base(0,0)
    ship1=Spacecraft('Target')
    
    obj_x=0.0
    obj_y=0.0
    obj_vx=0.0
    obj_vy=0.0 

    running=True 
    dt=0.01
    t=0.
    while running :
        t+=dt
        obj_x,obj_y,obj_vx,obj_vy=physics(t)
        if obj_y<0. :
           running=False 
        else:
           ship1.set_position(obj_x,obj_y)
           ship1.set_velocity(obj_vx,obj_vy)
           base1.add_traj_data((obj_x,obj_y))
#
#       Do something
#
           base1.approx_traj(3)
        
#
#       Do something
#
           if missile1.fired==False:
              base1.intercept(missile1)
#
#       Do something
#        
              missile1.firing()
           missile1.update(dt)
           print "Obj:%f %f " % (obj_x,obj_y)
           print "Mis:%f %f " % missile1.get_position()

        
if __name__=='__main__':
    main()
        


    
