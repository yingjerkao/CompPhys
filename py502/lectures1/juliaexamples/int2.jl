# Incorrectly modified version of int1.jl.
# Here the statement b=a+1 will cause an error, because the constant 1 is of the
# default integer type Int64 and a+1 will also be of this type because UInt32 is
# too small. Since b is declaired as UInt32, it cannot hold the result and
# the program crashes when run. An error message is produced.

function integertest()
   a::UInt32=typemax(UInt32)
   b::UInt32=1
   b=a+1
   return a,b
end

x,y=integertest()
println(x)
println(y)
