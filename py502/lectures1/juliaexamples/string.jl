# Illustration of string with characters of different length
# ASCII characters use 1 byte each
# Chinese characters need 2 bytes each
# A string stores only as many bytes as needed for each character 
# - unlike objecys of Char type, which are always 4 bytes

# Working with a string of mixed Chinese and ASCII characters:

 a="小写abc大写ABC"

 n=length(a)     # This is the number of characters in the string
 m=lastindex(a)  # This is the length of the string in bytes; elements a[1],...,a[n]
                 # [There is also a firstindex() function but here the first will be 1]

 println("Number of characters is:  ",n)
 println("Number of bytes (indices) is:  ",m)

# An index that does not correspond to the starting index of a character cannot be shown
# This loop illustrates the method of 'catching' errors
# - error thrown by the 'throw' function (see ifelse.jl) are caught this way
# - see also example in program catch.jl

 for i = 1:m
    try 
       println(i,"  ",a[i])
       # what follow 'try' is executed if that does not cause an error
    catch
       println(i,"   no character starts at this position")
       # what follows 'catch' is executed if 'try' causes an error; here doing nothing
    end
 end
 println()

# This is another way to show the actual individual characters
# But then we do not have access to the indices (byte number)

 for c in a
    println(c)     
 end

