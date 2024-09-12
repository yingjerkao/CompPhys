import numpy as np
import scipy as sp


class Radar:
    """ A Radar station which tracks a moving object and update
        the angle """
    def __init__(self,x,y):
        self.angle=0.0
        self.x=x
        self.y=y
        
    def update_angle(self, angle):
        """ Update the current angle"""
        self.angle=angle

    def get_angle(self):
        return self.angle
        

class Radar_Array():
    """
    A Radar system with two radar stations separated by a distance d to
    track moving objects.
    Radar station A is located at (0,0) and B is located at (a,0)
    Their readings are alpha and beta respectively
    
    """
    def __init__(self,x1=0,y1=0,x2=100,y2=0):
        self.alphas=[] # Angle of Radar A
        self.betas=[]  # Angle of Radar B
        self.velo_x=0.0 # Velocity of the moving object
        self.velo_y=0.0 #
        self.x=0.0 # Position of the moving object
        self.y=0.0 #
        self.climb_angle=0.0 # Climb angle of the moving object
        self.radarA=Radar(x1,y1)
        self.radarB=Radar(x2,y2)
        

    def update_reading(self):
        """ Update the lists of the reading angles from radar A and B"""
        pass


    def update_info(self):
        """ Use the current set of readings, obtain the current position
            ,velocity and the climb angle of the moving object"""
        pass

    def get_info(self):
        """ Return the current position, velocity and climb angle of
            the moving object"""
        pass
