# Function with one argument (type not specified, wil work for types that 'make sense')
# Showing examples of complex type declarations and functions of complex numbers

 function complexoperations(c)
    c1::ComplexF32=c     # same as c1::Complex{Float32}=c
    c2::ComplexF64=c^2   # same as c2::Complex{Float64}=c^2
    d1=abs(c1)           # the radius in polar notation
    d2=angle(c1)         # the angle in polar notation
    d3=round(c1)         # example of rounding a complex number
    return c1,c2,d1,d2,d3
 end

# In the first assignment below, c is a default complex type (ComplexF64, same as Complex{Float64})
# In the second assignemnt, c becomes a 4-tuple returned by the function (example of dynamic typing)

 c=complex(1.25,2.8)          # same as c=1.0+2.5im     
 c=complexoperations(2c)      # numerical constants as factors in front of variables 
                              # do not need * (but this is some times confusing; I avoid it)
 println(c)                   
 println()
 
# this is one way to go through all elements of a 'collection' (here a 4-tuple)

 for d in c                  
     println(typeof(d)," :   ",d)
 end

