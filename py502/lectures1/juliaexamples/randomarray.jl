# A function makerandom with two methods is declared.
# This looks just like two functions with the same name but with different arguments.
# An array r with n Float64 elements is declared; element i is referred to as r[i].
# The Base function round(T,m) rounds the number m to the closest integer and converts to type T (here Int)
# The Base function rand() generates (when given no arguments) a random Float64 in [0,1).
# The functional difference between the methods is Float64 (first) vs Float32 (second) numbers returned.
# In the second method r[i]=rand() implies a loss of precision from 64 to 32 bit Float.

 function makerandom(n::Int)
    r=Array{Float64}(undef,n)
    for i=1:n
       r[i]=rand()
    end
    return r
 end

 function makerandom(m::Float64)
    n=round(Int,m)
    r=Array{Float32}(undef,n)
    for i=1:n
       r[i]=rand()
    end
    return r
 end

# The function is called twice, with different arguments (example of multiple dispatch).
# In each case 5 times; n is assigned an integer-constant value, type will be Int (Int64).
# The Base function convert(Float64,n) converts the integer n to a Float64.

 n=5
 m=convert(Float64,n)

# The function is called with Int argument (first method dispatched)
# a will be the 5-element Float64 array returned by the function

 a=makerandom(n)
 for i=1:n
    println(i,"  ",a[i])
 end

# The function is called with Float64 argument (second method dispatched)
# b will be the 5-element Float32 array returned by the function

 a=makerandom(m)
 for i=1:n
    println(i,"  ",a[i])
 end

