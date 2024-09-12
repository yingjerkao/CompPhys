# Problem Set 10
# Student ID: r99222024
# Collaborators' ID: r99222024
# Time: 00:10
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

    def get_angle(self)
        return self.angle
        

class Radar_Array():
    """
    A Radar system with two radar stations separated by a distance d to
    track moving objects.
    Radar station A is located at (0,0) and B is located at (d,0)
    Their readings are alpha and beta respectively
    
    """
    def __init__(self,x1=0,y1=0,x2=d,y2=0):
        self.alphas=[]
        self.betas=[]
        self.velo_x=0.0
        self.velo_y=0.0
        self.x=0.0
        self.y=0.0
        self.radarA=Radar(x1,y1)
        self.radarB=Radar(x2,y2)


    def update_reading(self):
        """ Update the lists of the reading angles from radar A and B"""
        pass


    def update_info(self):
        """ Use the current set of readings, obtain the current position
            and  velocity of the moving object"""
        pass

    def get_info(self):
        """ Return the current position and velocity of the moving object"""
        pass
