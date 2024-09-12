import math

def grule( n ):
    """Compute roots and weights for nth degree Legendre polynomial.

    USAGE:
        ( x, w ) = grule( n )

    INPUT:
        n       - degree of Legendre polynomial

    OUTPUT:
        x       - array of roots.  The roots of the polynomial are symmetric
                  about the origin so only the non-negative roots are returned.
	w       - Array of weights.  w[i] is paired with both x[i] and -x[i].

    NOTES:
        I'm no longer sure, but I think this came from A.H. Stroud, and
        Don Secrest, "Gaussian Quadrature Formulas", Prentice-Hall,
        Englewood Cliffs, N.J., 1966.  This was taken from FORTRAN
        code (as its appearence suggests).  It was converted to C by
        J. Senning in 1986 (I think...) and then into a MatLab
        (Octave) M file in February 1999.

    AUTHOR:
        Jonathan R. Senning <jonathan.senning@gordon.edu>
        Gordon College
        February 21, 1999
        Converted to Python September 2008
    """

    m = (n+1)/2
    e1 = n*(n+1)

    x = []
    w = []

    for i in xrange( m ):
        t    = (4*i+3)*math.pi/(4*n+2)
        x0   = (1.0-(1.0-1.0/n)/(8.0*n*n))*math.cos(t)
        pkm1 = 1.0
        pk   = x0

        for k in xrange( 2, n + 1 ):
            t1 = x0*pk
            pkp1 = t1-pkm1-(t1-pkm1)/k+t1
            pkm1 = pk
            pk = pkp1

        den  = 1.0-x0*x0
        d1   = n*(pkm1-x0*pk)
        dpn  = d1/den
        d2pn = (2.0*x0*dpn-e1*pk)/den
        d3pn = (4.0*x0*d2pn+(2.0-e1)*dpn)/den
        d4pn = (6.0*x0*d3pn+(6.0-e1)*d2pn)/den
        u    = pk/dpn
        v    = d2pn/dpn
        h    = -u*(1.0+0.5*u*(v+u*(v*v-d3pn/(3.0*dpn))))
        p    = pk+h*(dpn+0.5*h*(d2pn+h/3.0*(d3pn+0.25*h*d4pn)))
        dp   = dpn+h*(d2pn+0.5*h*(d3pn+h*d4pn/3.0))
        h    = h-p/dp
        fx   = d1-h*e1*(pk+0.5*h*(dpn+h/3.0*(d2pn+0.25*h*(d3pn+0.2*h*d4pn))))
        x.append(x0+h)
        w.append(2.0*(1.0-x[i]*x[i])/(fx*fx))

    if ( m+m > n ):
        x[m-1] = 0.0

    return ( x, w )
