# Illustration of constructor creating a composite type using "struct"
# The name of the struct is System, and objects of the type System will
# have 3 different fields (of 3 different types). The fields of an object a 
# which has been declared to be of the type System will be accessed as
# a.size, a.temp, and a.conf. The elements of the .conf field are
# accessed as the elements of any vector; a.conf[i].

struct System
   size::Int
   temp::Float64
   conf::Array{Int,1}   # 1D array which later can take any size
end

# The function below will be used to initalize a configuration, which will
# be initially assigned to the .conf field of an object of the System type.

function randomconf(n)
   s=Array{Int}(undef,n)
   for i=1:n
      s[i]=rand(0:1)   # the configuration will just consist of os and 1s
   end
   return s
end

# The function below will be used to update the .conf field of an object 
# c of the System type, using the other fields of the struct as well.
# The stochastic process has a tendency to flip 1s to 0s but will
# not flip 0s to 1s, using a probability depending on c.temp.
# The updated configuration is returned.

function updateconf(c::System)
   for i=1:c.size
      if rand() > exp(-c.temp*c.conf[i])
         c.conf[i] = 1-c.conf[i]
      end
   end
   return c
end

# This function completes a "simulation" on the onject c of type System
# Prints the updated configuration after each updating sweep.

function simulation(m,c::System)
   for i=1:m
      c=updateconf(c)
      println(c.conf)
   end
   return nothing
end

n=10

# Initializing an onject a of composite type System
# Prints the field names and contents of the fields for inspection

a=System(n,0.1,randomconf(n))
println(fieldnames(System))       # the function fieldnames returns the field names
println(a.size)
println(a.temp)
println(a.conf)
println()

# Proceeding to carry out a simulation consisting of 20 updating sweeps

simulation(20,a)

