# A function illustrating the if-elseif-else control construct
# The "throw" function is an example of a customized exception handling
# DomainError is a built-in exception (function) and it's given a custimized message here

 function testnumber(a::Int)
    if a==8 || a==88
       luck=1
    elseif a==13 || a==4
       luck=-1
    elseif a>=1 && a<=99
       luck=0
    else
       throw(DomainError(a,"Argument must be between 1 and 99"))       
    end
 end

# reading from stdin, parsing as integer, calling the testnumber function

 println("Give an integer between 1 and 99")
 a=parse(Int,readline(stdin))
 happy=testnumber(a)

 if happy==0
    println("Neutral number")
 else
    msg = (happy==1 ? "Lucky number, congratulations!" : "Unlucky number, too bad!")
    println(msg)
 end

# The "msg = ..." expression uses the so-called "ternary operator"
# X & Y : Z means "if X is true, Y is evaluated, if X is false, Z is evaluated"
