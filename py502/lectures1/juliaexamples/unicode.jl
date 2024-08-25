# Demonstration of ASCII and Unicode echaracters

# The ASCII system is based on the integers 0-127 (stored in 1 byte)
# Some ASCII characters are not visible, e.g., \u7 is the 'bell' sound [try println('\u7')] 

# The Unicode system encodes characters using 1-4 bytes
# Currently valid characters are between 0 and D7FF (hexadecimal) as well as E000 to 10FFFF
# Not all of them actually contain any characters; those in the higher range may not show properly
# The ASCII characters are the first 128 Unicode characters

# The function Char(c) gives the character corresponding to integer c
# This piece of code shows all the ASCII characters 
# Randomly chosen Unicode characters from the lower range are also shown

 c1=0x0              # 0x followed by digits 0-F for hexadecimal notation    
 c2=0xD7FF
 for i=0:127
    c=rand(c1:c2)    # with the argument c1:c2, rand generates integers between c1 and c2   
    println(i,"  ",Char(i),"     ",c,"  ",Char(c))
 end








