# This function creates an n*n random matrix (similar to randomarray.jl but 2-dim array)

 function randmatrix(n::Int)
    mat=Array{Float64}(undef,n,n)
    for j=1:n
       for i=1:n
          mat[i,j]=rand()
       end
    end
    return mat
 end

# Ask for matrix size and read it (stdin = standard input) using readline
# Text input has to be parsed to a type (here Int)

 println("Give matrix size")
 n=parse(Int,readline(stdin))

# Create two random matrices and their product
# Note that "*" is actual matrix multiplication

 a=randmatrix(n)
 b=randmatrix(n)
 c=a*b

# print the results

 println()
 println("A, B, A*B")
 for i=1:n
    println(a[i,:],"  ",b[i,:],"  ",c[i,:])
 end

# Element-by-element operations can be done with "." added to oerator
# Here element-by-element multiplication

 c=a.*b
 println()
 println("A, B, A elements multiplied by B elements")
 for i=1:n
    println(a[i,:],"  ",b[i,:],"  ",c[i,:])
 end


# Matrix inverse using Base function inv()
# Multiply inverse of A by A to check if OK

 b=inv(a)
 c=a*b
 println()
 println("A, 1/A, A*(1/A)")
 for i=1:n
    println(a[i,:],"  ",b[i,:],"  ",c[i,:])
 end
