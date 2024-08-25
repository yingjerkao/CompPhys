# A function with no arguments is declared
# In the function two unsigned 32-bit integers are declared and given values
# The internal typemax function delivers the largest value representable by the given type
# The variables following the return statement are returned 

function integertest()
   a::UInt32=typemax(UInt32)
   b::UInt32=1
   c=a+b
   return a,c
end

# This is the "main program"
# x,y are given by the values returned by integertest
# Output is written using the println function

x,y=integertest()
println(x)
println(y)

# Output should be
# $ 4294967295
# $ 0
#

# Illustrates the "wrap-around" (mod 2^{32}) behavior of integers
# To illustrate the behavior for signed integers, modify by changing UInt32 in the declarations to Int32
