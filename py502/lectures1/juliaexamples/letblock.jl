# Use of a "let" block to save a value in a function between function calls
# The let block is inside a module in which a random-number generator is defined
# The function ran64 has two methods:
# - ran64(seed) initializes the integer to seed
# - ran64() generates the next integer and returns it

module RanLcg

export ran64

const a = convert(UInt64,2862933555777941757)  # a and c are global constants
const c = convert(UInt64,2862933555777941757)  # visible only inside the module

let

    r = Ref(convert(UInt64,1))          # r is a reference (pointer) to a given type

    global function ran64(seed::Int)
       r[]=convert(UInt64,seed)         # the value stired at r is accessed as r[]
    end                                 # would be r[i] for element i of an array, but
                                        # here r points to a single float which is like a
    global function ran64()             # 0-dimensional array and doesn't need an index
       r[]=r[]*a+c
    end

end # let

end # module

function manyrandom(n)  # this function just calls ran64() n+1 times
   for i=1:n
      ran64()
   end
   println(ran64())     #  print the last value
end

using .RanLcg

n=10^8   # The number of random numbers to be generated (last one printed)

# iterate n times inside the main program, timing it to check efficiency

ran64(5373731)  # initialize ran64
@time begin
   for i=1:n    # try to replace n by its actual value and see if time changes!
      ran64()
   end
   println(ran64())
end

# iterate n times inside a function, timing it to check efficiency (improvement)

ran64(5373731)  # initialize ran64 with same seed as before
@time begin
   manyrandom(n)
end
