# Illustration of local scope of variables
# Also illustrates unmutable and mutable objects

 function func2(a,c)    # a is in the argument list, becomes local of func2()

    function func1()
       println("Hello from func1, a = ",a)      # a==2 here
       a=1                                    
       println("Hello from func1, a = ",a)      # now a==1
       for i=1:1
          b=i                                   # no local b exists before, b is local to for loop
          println("Hello from func1, b = ",b)   # b==1 here
       end
       println("Hello from func1, b = ",b)      # there is no local visble b here, b==3 is the global b
       println()
    end

    a=2               # assignment to local a
    func1()
    println("Hello from func2, a = ",a)   # func1() changes the value of a, now a==1
    c .= 1

 end

 a=3
 b=3
 c=zeros(Int,2)
 func2(a,c)
 println("Hello from the main program, a = ",a)   # global a is unmutable, retains value a==3
 println("Hello from the main program, c = ",c)   # array c is mutable, values have been changed by func2()

