set yr [0:1.2]
set xr [0:2]
set title "Mean Field Solution: Ising Model"
set xlabel "m"
#set term postscript eps color lw 2
set term pdf color 
set output 'MFIsing.pdf'
plot x title 'm', tanh(x/2) title 'T=2T_c', tanh(x/1) title 'T=T_c', tanh(x/0.5) title 'T=0.5T_c'
set term pop
