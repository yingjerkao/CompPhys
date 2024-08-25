# Program exemplifying loops and vector operators, comparing execution time
# time_ns() is a Base function giving the time on nan-second since computer turned on

# This function makes a vector of n float values

 function makevector(n)
    r=Array{Float64}(undef,n)
    for i=1:n
       r[i]=i/n
    end
    return r
 end

# Making float vector and times a loop performed on its elements; ran[i]=ran[i]^2
# Takes vector size from global varianle n (not recommended)

 function test0()
    ran=makevector(n)
    t0=time_ns()
    for i=1:n
       ran[i]=ran[i]^2 
    end
    t1=(time_ns()-t0)/n
    s=sum(ran)
    return t1,s
 end

# Making float vector and times a loop performed on its elements; ran[i]=ran[i]^2
# The vector size is an argument; n local

 function test1(n::Int)
    ran=makevector(n)
    t0=time_ns()
    for i=1:n
       ran[i]=ran[i]^2 
    end
    t1=(time_ns()-t0)/n
    s=sum(ran)
    return t1,s
 end

# Making float vector and times vectorized operation its elements; ran[:].=ran[:].^2
# Uses [:] to indicate elements of 1-dim array

 function test2(n::Int)
    ran=makevector(n)
    t0=time_ns()
    ran[:].=ran[:].^2
    t1=(time_ns()-t0)/n
    s=sum(ran)
    return t1,s
 end

# Making float vector and times vectorized operation its elements; ran.=ran.^2
# No reference to dimension of vector needed

 function test3(n::Int)
    ran=makevector(n)
    t0=time_ns()
    ran.=ran.^2
    t1=(time_ns()-t0)/n
    s=sum(ran)
    return t1,s
 end

# Making float vector and times macro operation its elements; ran=ran^2

 function test4(n::Int)
    ran=makevector(n)
    t0=time_ns()
    @. ran=ran^2
    t1=(time_ns()-t0)/n
    s=sum(ran)
    return t1,s
 end

 n=1000000

# Carries out all tests 3 times
# Uses @time macro to measure time of entire set of tests each time

 for i=1:5
    println(i)
    @time begin
       println("0, time (ns) per operation: ",test0())
       println("1, time (ns) per operation: ",test1(n))
       println("2, time (ns) per operation: ",test2(n))
       println("3, time (ns) per operation: ",test3(n))
       println("4, time (ns) per operation: ",test4(n))
    end
    println()
 end



