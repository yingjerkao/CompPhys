# Illustration of the try-catch functionality
# - errors thrown by the 'throw' function (see ifelse.jl) are caught this way

 for i = -4:4
    try              # trying to execute what's next, if an error is thrown go to the catch part
       s=sqrt(-i)
       println(i,"  ",s)
    catch            # what follows is executed only if an error was thrown in 'try'
       println(i," error, negative argument")
    end
 end

