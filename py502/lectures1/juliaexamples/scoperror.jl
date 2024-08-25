# Illustration of soft and hard local scope

# A function creates a hard local scope, which implies that a new 
# object "a" is assigned which is different from the existing global a.

 function afunc()
    a=0
    for i=1:5
       a=a+1
       println("A  ",i,"  ",a)
    end
 end

 afunc()
 println()

# A for block creates a local soft scope, which implies that a new object "a"
# cannot be assigned if there is an existing global a. "global a" then has to
# be used to indicate that the global variable is to be used.

 a=0
 for i=1:5
    global a=a+1
    println("B  ",i,"  ",a)
 end

# If "global a" is not used in the for block, then a=a+1 must refer
# to a local variable, but since local a on the righ-hand side does not
# yet exist there is an error here.

 a=0
 for i=1:5
    a=a+1
    println("C  ",i,"  ",a)
 end

# Note that this loop work if run in REPL, which for good reasons has
# a slightly different rule for soft scopes.

# In practice, many loops in Julia has to be placed inside functions
# in order to avoid this problem (which really is intended as a mechanism
# to avoid certain errors - see Julia documentation).
