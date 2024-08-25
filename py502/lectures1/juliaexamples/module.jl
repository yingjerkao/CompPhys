# Illustrates aspects of modules
# The module named DemoModule exports the function func1
# There is a global variable a which takes the value 10 after
# the code in the module has been executed (at the using statement in main.jl)

module DemoModule

export func1

function func0(n)
   return 10*n
end

function func1(n)
   return a*n+1
end

a=func0(1)
println("In DemoModule global a has the value  ",a)

end  # of module