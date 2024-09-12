# Problem Set 9
# Student ID: r99222024
# Collaborators' ID: r99222024
# Time: 00:10

class Spacecraft(object):
    """
    A spacecraft is initialized with its dimensions height, width, and depth,
    weight, name and the coordinates and velocity of the center of mass.
    
    """
    def __init__(self, name='',x=0.,y=0.,velo_x=0.,velo_y=0.,fuel=10,width=5., height=5.):
        """ Initialize parameters """
        self.name=name
        self.x=x
        self.y=y
        self.velo_x=velo_x
        self.velo_y=velo_y
        self.height=height #height is the dimemsion in y direction
        self.width=width   #width is the dimemsion in x direction
        self.fuel=fuel
        self.fuel_max=10

    def refuel(self,fuellevel=10):
        """ Refuel the fuel tank """
        self.fuel=fuellevel

    def position(self):
        """ Retrun position of the ship as (x, y)"""
        return x,y

    def set_position(self, x, y):
        """ Set the position of the ship, with no return"""
        self.x=x
        self.y=y
         

    def velocity(self):
        """ Return velocity of the ship as (Vx, Vy)"""
        return velo_x,velo_y
        
    def set_velocity(self,v_x, v_y):
        """ Set the ship velocity, with no return """
        self.velo_x=v_x
        self.velo_y=v_y

    def size(self):   
        """ Retrun the size of the ship as (height, width) """
        return (height, width)

    def fuel_level(self):
        """ Return current fuel_level in type int """
        pass

    def get_name(self):
        """ Retrun name of the ship in type string"""
        return self.name
        
    def __str__(self):
        """
        Return the string representation for the spacecraft.
        The string representation for a spaceship called
        'Enterprise' with height=3.0 and width=4.0 and at (x, y)=(7, 8)
        should be:
		Enterprise: (height,width)=(3.0, 4.0) and (x,y) = (7, 8)
        """
	return '%s: (%f,%f) and (%d, %d)' % (self.name, self.height, self.width, self.x, self.y)
	
    def __cmp__(self,other):
        """
        Compare the two spacecrafts, use the built-in function cmp(), return 1, 0, -1 as defined in cmp() fucntion.
        """
        return cmp(self.height*self.width, other.height*other.width)

def accelerateShip(craft, acc):
	"""
	Increase the velocity of 'craft' by the quantity 'acc', with no return.
	acc = (dVx, dVy) is a tuple of the change of velocity in x and y directions.
	The final velocity Vf = Vi + acc, Vi is the original velocity.
	"""

def isCollision(craft1, craft2):
	"""
	Check whether 'craft1' collides with 'craft2', return True or False in type boolean.
	"""

