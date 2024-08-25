!-----------------------------------------------------!
!This program generates a 2D color intensity plot.    !
!Values of a function f(x,y) are read from a file.    !
!The file should have m*n function values (one value  ! 
!per line) corresponding to m x-values and n y-values.! 
!The output is given in the postscript file 'gr.ps'.  !
!-----------------------------------------------------!
 program colorplot2d
!-------------------!
 implicit none

 integer :: i,j,m,n
 real    :: lx
 real, allocatable :: a(:,:)
 character(32) :: fname

 print*,'Input file'
 read*,fname
 print*,'X and Y sizes of the matrix'
 read*,m,n
 print*,'Desired width of the plot (in points)'
 read*,lx
 
 open(1,file=fname,status='old')
 allocate(a(m,n))
 do j=1,n
    do i=1,m
       read(1,*)a(i,j)
    end do
 end do
 close(1)

 call initgraph(lx,m,n)
 call plotmatrix(a,m,n)
 call closegraph()

 deallocate(a)

 end program colorplot2d
!-----------------------!

!----------------------------!
 subroutine plotmatrix(a,m,n)
!----------------------------!
 implicit none
 
 integer :: i,j,m,n
 real    :: a(m,n),amax,amin,aa,ar,ag,ab

 amax=maxval(a)
 amin=minval(a)
 do j=1,n
    do i=1,m
       aa=(a(i,j)-amin)/(amax-amin)
       call setcolor(aa,ar,ag,ab)
       write(2,1)i,j,ar,ag,ab,' p'
       1 format(2i5,' ',3f5.2,a)
    end do
 end do

 end subroutine plotmatrix
!-------------------------!


!------------------------------!
 subroutine initgraph(lx,nx,ny)
!------------------------------!
 implicit none

 integer :: nx,ny
 real    :: lx,p

 p=100.d0/real(nx) 
 open(2,file='gr.ps',status='replace')
 1 format(a)
 write(2,1)'%!'
 write(2,*)'100 200 translate'
 write(2,2)lx/nx,lx/nx,' scale'
 2 format(f7.2,' ',f7.2,' ',a)
 write(2,*)'0 0 moveto ',nx+1,' 0 rlineto 0 ',ny+1,' rlineto'
 write(2,*)-nx-1,' 0 rlineto closepath fill'
 write(2,*)'1.1 setlinewidth -0.55 -0.05 translate' 
 write(2,*)'/p {setrgbcolor moveto 1.1 0 rlineto stroke} def'

 end subroutine initgraph
!------------------------! 

!-----------------------! 
 subroutine closegraph()
!-----------------------! 

 write(2,*)'showpage'
 close(2)

 end subroutine closegraph
!-------------------------! 


!-------------------------------!
 subroutine setcolor(a,rc,gc,bc)
!-------------------------------!
 implicit none

 real, parameter :: f1=1.d0/4.d0
 real, parameter :: f2=2.d0/4.d0
 real, parameter :: f3=3.d0/4.d0
 
 real :: a,r,g,b,rc,bc,gc,aa

 if (a > 1.) then
    rc=1.
    gc=1.
    bc=1.
 else if (a < f1) then
    r=0.
    g=0.
    b=0.75*a/f1
 else if (a < f2) then
    r=((a-f1)/f1)**0.5
    g=0.
    b=0.75*(1-(a-f1)/f1)
 else if (a < f3) then
    r=1.
    g=(a-f2)/f1
    b=0.
 else
    r=1.
    g=1.
    b=(a-f3)/f1
 end if
 aa=a**0.2
 rc=r*aa
 gc=g*aa
 bc=b*aa

 end subroutine setcolor
!-----------------------! 
