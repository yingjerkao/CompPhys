# Function with boolean argument, prints illustrations of operations combining Bool and Int types
# Bool is a subset of Int and can be sibject to integer math with true/false equivalent to 1/0
# Note that one Bool uses 8 bits (one byte; same as Int8).

 function trueorfalse(b::Bool)
     println(b)
     println(b*1)
     println(b*2)
     println(b*true)
 end

# Calling the function with both 'true' and 'false' arguments
# note that these are reserved words in Jula (can never be redefined)

 trueorfalse(true)
 println()
 trueorfalse(false)
