# using a package available after adding it with the Julia package manager
# The 1-d integration package QuadGK has been added by add QuadGK
# It can now be used in any Julia code

using QuadGK

function func(x)    # some non-tr0vial function for illustration
   return log(x)*cos(x)+x^2
end

# Integrating the function between 0 and 1, using different tolerances
# - convergence observed when the tolerance becomes small

for i=1:10
   t=1/10.0^i
   res,err=quadgk(func,0,pi,rtol=t)
   println(i,"  ",res,"  ",err)
end
