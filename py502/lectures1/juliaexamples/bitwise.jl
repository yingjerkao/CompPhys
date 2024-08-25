# Base function bitstring(x) converts the argument x into a string of 0s and 1s.
# Using this function to illustrate biwise boolean operations

a=123456789
b=-987654321

println("              a  ",bitstring(a))
println("              b  ",bitstring(b))

# bitwise and,or,xor

println()
println("bitwise a and b  ",bitstring(a & b))
println("bitwise  a or b  ",bitstring(a | b))
println("bitwise a xor b  ",bitstring(xor(a,b)))

# bitshift operations

println()
println("                              b  ",bitstring(b))
println("left bit shift of b              ",bitstring(b << 5))
println("right arithmetic bit shift of b  ",bitstring(b >> 5))
println("right logical bit shift of b     ",bitstring(b >>> 5))

# The arithmetic right bit shift keeps the sign bit
# The logical right bit shift affects all bits
# Bith shifts can be used for integer multiplication and division by powers of 2
# - some times faster than * and /
