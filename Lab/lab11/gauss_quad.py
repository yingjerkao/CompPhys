from grule import grule

def gauss_quad( f, a, b, n ):
    """ Estimate the integral of f(x) from a to b using Gaussian Quadrature.

    USAGE:
        y = gauss_quad( f, a, b, n )

    INPUT:
        f       - function to integrate
        [a, b]  - interval of integration
        n       - number of nodes (points to evaluate at)

    OUTPUT:
        float y - estimate of integral of f(x) from a to b

    NOTES:
        Uses gaussian quadrature to estimate the integral of f from a to b
        using n nodes.  The interval [a,b] is mapped to the interval [-1,1].

        The change in interval is made by the substitution
            t = 2*(x-a)/(b-a)-1 
        where x is in [a,b] and t is in [-1,1].  Solving this for x gives
        x = 0.5*(b-a) * t + 0.5*(b+a).  Thus dx = 0.5*(b-a) * dt.  So

            / b                / 1
            |            (b-a) |
            | f(x) dx  = ----- | f( 0.5*(b-a) * t + 0.5*(b+a) ) dt
            |              2   |
            / a                /-1

    AUTHOR:
        Jonathan R. Senning <jonathan.senning@gordon.edu>
        Gordon College
        February 22, 1999
        Converted to Python September 2008
    """

    # Call grule() to generate the nodes and weights.  Only (n+1)/2 nodes and
    # (n+1)/2 weights are returned, taking advantage of the symmetry of the
    # roots of the Legendre polynomials.
	        
    ( r, w ) = grule( n )

    # Compute some useful quantities and initialize the sum.  If the number
    # of nodes is odd then the sum is initialized to w((n+1)/2) * f((b+a)/2),
    # accounting for the node r = 0.  If the number of points requested is
    # even then the sum is initialized to zero.

    alpha = 0.5 * ( b - a )
    beta  = 0.5 * ( b + a )

    if ( 2 * ( n / 2 ) == n ):
        sum = 0.0
    else:
        sum = w[(n-1)/2] * f( beta )

    # Compute the sum and return the estimate of the integral

    for i in xrange( n / 2 ):
        x0 = -alpha * r[i] + beta
        x1 =  alpha * r[i] + beta
        sum = sum + w[i] * ( f( x0 ) + f( x1 ) )

    y = alpha * sum

    return y

if __name__=="__main__":
    from math import *
    def f(x):
        return exp(x)*cos(x)
    exact=0.5*(exp(1)*(sin(1)+cos(1))-exp(-1)*(sin(-1)+cos(-1)))
    gauss=gauss_quad(f, -1,1,3)
    print "Exact:",exact
    print "Gauss Quadrature:",gauss
    print "Error:", abs(gauss-exact)
    
