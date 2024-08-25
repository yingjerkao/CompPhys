# Illustration of the use of a module imported from a local file module.jl
# The code in the module appears to the compiler at the include statement
# and is executed. In this case a function named func1 is exported and is
# therefore accessible by this name. The function func0 is not exported 
# but is still accessible by the name DemoModule.func0
# Note that global variables with the name "a" appear in both the moduke
# and the main program; they belong to different names spaces and are only
# visible in their own name scapes

 include("module.jl")

 using .DemoModule

 a=5
 println("In the main program global a has the value  ",a)
 println("Function calls:")
 println("func1:  ",func1(2))
 println("func0:  ",DemoModule.func0(1))


