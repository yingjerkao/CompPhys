# Calculates pi using a circle with radius r=1/2 (slightly faster than r=1) by MC sampling.

function pionebin(n) # samples and computes the average for one bin with n points
   sum=0
   for i=1:n
      x2=(rand()-0.5)^2
      y2=(rand()-0.5)^2
      if x2+y2 <= 0.25 
         sum=sum+1
      end
   end
   return 4.0*sum/n
end

function samplepi(nbin,nsamp)  # Doing MC sampling of nbin bins, each sampling nsamp points
   av=0.
   er=0.    
   for j=1:nbin
      p=pionebin(nsamp)
      av=av+p
      er=er+p^2
      println(j,"   ",p)
   end
   av=av/nbin
   er=er/nbin
   er=((er-av^2)/(nbin-1))^0.5
   return av,er
end

nbin=10
nsamp=10000

ap,ep=samplepi(nbin,nsamp)

println()
println("Final result and error:   ",ap,"   ",ep)
