# Illustration of Romberg integration
# Shows convergence vs the number of trapezoidal (or midpoint) integrations

 function func(x)   # Function to be integrated
#    return exp(x)*sin(x)*log(cos(x*100)+2)
    return exp(x)  
 end

 function pextrapolate(val)  # Polynomial extrapolation (Lagrange) based on numbers in vector val
    n=length(val)-1  # take n from size of vector
    p0=0.  
    for k=0:n
       p=1.
       for j=0:n
          if j != k 
             p=p/(2.0^(2*(j-k))-1)
          end
       end
      p0=p0+p*val[k+1]*(-1)^n
    end
    return p0
 end

 function gridsum(func,x1,dx,nx,fsum)   # summing over grid points
    for i=0:nx-1
       fsum=fsum+func(x1+i*dx)
    end
    return fsum
 end

 function romberg1(func,x1,x2,n0)   # closed inteval Romberg
    n=n0-1
    dx=(x2-x1)/n0    
    fsum=(func(x1)+func(x2))/2
    fsum=gridsum(func,x1+dx,dx,n,fsum) 
    val=Vector{Float64}()
    push!(val,dx*fsum)
    println(0,"  ",val[1])
    m=n
    for i=1:15      
       if i==1
          n=n+1
          m=m+n
       else
         n=m+1
         m=m+n
         dx=dx/2
       end
       fsum=gridsum(func,x1+dx/2,dx,n,fsum) 
       push!(val,0.5*dx*fsum)
       println(i,"  ",val[i+1],"  ",pextrapolate(val))
    end
 end

 function romberg2(func,x1,x2,n0)   # open interval Romberg
    n=n0-1
    dx=(x2-x1)/n0 
    dsum=(func(x1+dx)+func(x2-dx))/2
    fsum=gridsum(func,x1+dx,dx,n,dsum) 
    val=Vector{Float64}()
    push!(val,dx*fsum)
    println(0,"  ",val[1])
    m=n
    for i=1:25  
       if i==1
          n=n+1
          m=m+n
       else
         n=m+1
         m=m+n
         dx=dx/2
       end
       fsum=fsum-dsum
       dsum=(func(x1+dx/2)+func(x2-dx/2))/2       
       fsum=fsum+dsum
       fsum=gridsum(func,x1+dx/2,dx,n,fsum) 
       push!(val,0.5*dx*fsum)
       println(i,"  ",val[i+1],"  ",pextrapolate(val))
    end
 end

 romberg1(func,0.,1.,10)
