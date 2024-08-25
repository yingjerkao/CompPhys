# This function opens a file containing a label (number) given in the
# argument as fnum, using 'interpolation' with $fnum, which converts fnum 
# to a segment of the string constructed with the string() function.
# Data contained in the 2*n=element array data are for illustration purposes
# written in ASCII format by the println() function and also in binary format 
# by write() - files are called "ranX.dat" and "binX.dat, respectively, 
# for file number X.

 function writedata(fnum,data)
    fname1=string("ran","$fnum",".dat")  
    fname2=string("bin","$fnum",".dat")  
    file1=open(fname1,"a")
    file2=open(fname2,"a")
    for i=1:size(data,2)
        println(file1,data[1,i],"  ",data[2,i])   # writing ACII formatted data
        write(file2,data[:,i])                    # writing binary data
    end     
    close(file1)
    close(file2)
 end

# This function makes a vector with n random numbers in [0,1)

 function makerandom(n)
    r=Array{Float64}(undef,n)
    for i=1:n
       r[i]=rand()
    end
    return r
 end

 println("How many data sets?")
 n=parse(Int,readline(stdin))

# Makes 5 different data sets related to the same random numbers
# Writing these to 5 different files using function writedata()

 d=Array{Float64}(undef,2,n)
 for i=1:5
    d[1,:]=makerandom(n)      # assigning with result of makerandom()
    d[2,:]=makerandom(n)      # assigning with result of makerandom()
    d[1,:]=d[1,:] .+ i        # doing +i operation these values
    d[2,:]=d[2,:].^i          # doing ^i operation these values
    writedata(i,d)            # calling the write function with index i
 end

