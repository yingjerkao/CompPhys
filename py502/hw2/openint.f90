!-------------------!
 program openintegration
!------------------------------------------------------------------------!
!This program integrates the function 1/(epsilon+x) from x=0 to a given 
!upper limit using two different open-interval integration formulas. The
!errors are calculated by subtracting the exact value of the integral. The
!integrations are carried out a number of times, with a number of 
!intervals N=N_0*2^n, where n=0,1,...,nmax. Since the number of points
!is doubled in each step, the value of the integral calculated at step n
!can be used in step n+1, for a time saving of approximately 50%.
!------------------------------------------------------------------------!
!The integrations are carried out in the subroutines 'integrate1' and 
!'integrate2'. The function is defined in the function 'func(x)', which
!uses values for the parameters 'alpha' and 'epsilon' stored in a
!common block.
!------------------------------------------------------------------------!
 implicit none

 integer, parameter :: maxstep=20

 real(8) :: epsilon,alpha
 common/funcblock/epsilon,alpha

 integer :: i,n0,steps
 real(8) :: x0,xn,integ1,integ2,iexact,dev1,dev2

 write(*,*)'Give e,a in function 1/(e+x)^a :'
 read(*,*)epsilon,alpha
 write(*,*)'Give upper integration end-point xn :'
 read(*,*)xn
 write(*,*)'Give number of intervals in first integration: '
 read(*,*)n0
 write(*,*)'Give number of point doublings :'
 read(*,*)steps

 x0=0.d0
 iexact=((epsilon+xn)**(1.d0-alpha)-epsilon**(1.d0-alpha))/(1.d0-alpha)

 do i=0,steps
    call integrate1(x0,xn,n0*2**i,i,integ1)
    call integrate2(x0,xn,n0*2**i,i,integ2)
    dev1=log(iexact-integ1)    
    dev2=log(iexact-integ2)    
    write(*,*)log((xn-x0)/dfloat(n0*2**i)),dev1,dev2
 end do

 end program openintegration
!---------------------------!

!-----------------------------------------!
 subroutine integrate1(x0,xn,n,step,integ)
!----------------------------------------------------------------------!
!Integration using order-h integration formula.
!The value of the integral calculated at step n is used in step n+1.
!Note that the coefficients for the boundary points have to be treated
!separately, as they will not have been calculated with the correct 
!coefficients in the previous step.
!----------------------------------------------------------------------!
 implicit none

 integer :: i,n,step
 real(8) :: x0,xn,h,integ,func

 h=(xn-x0)/dfloat(n)
 if (step==0) then
    integ=1.5d0*(func(x0+h)+func(xn-h))
    do i=2,n-2
       integ=integ+func(x0+dfloat(i)*h)
    enddo
 else
    integ=integ/(2.d0*h)-0.5d0*(func(x0+2.d0*h)+func(xn-2.d0*h))
    integ=integ+1.5d0*(func(x0+h)+func(xn-h))
    do i=3,n-3,2
       integ=integ+func(x0+dfloat(i)*h)
    enddo
 end if
 integ=integ*h

 end subroutine integrate1
!-------------------------!

!-----------------------------------------!
 subroutine integrate2(x0,xn,n,step,integ)
!----------------------------------------------------------------------!
!Integration using order-h^2 integration formula.
!The value of the integral calculated at step n is used in step n+1.
!Note that the coefficients for the boundary points have to be treated
!separately, as they will not have been calculated with the correct 
!coefficients in the previous step.
!----------------------------------------------------------------------!
 implicit none

 real(8), parameter :: a1=23.d0/12.d0
 real(8), parameter :: a2=7.d0/12.d0
 real(8), parameter :: b1=7.d0/12.d0-23.d0/12.d0
 real(8), parameter :: b2=1.d0-7.d0/12.d0

 integer :: i,n,step
 real(8) :: x0,xn,h,integ,func

 h=(xn-x0)/dfloat(n)
 if (step==0) then
    integ=a1*func(x0+h)+a2*func(x0+2*h)
    integ=integ+a1*func(xn-h)+a2*func(xn-2*h)
    do i=3,n-3
       integ=integ+func(x0+i*h)
    enddo
 else
    integ=integ/(2.d0*h)
    integ=integ+b1*(func(x0+2*h)+func(xn-2*h))
    integ=integ+b2*(func(x0+4*h)+func(xn-4*h))
    integ=integ+a1*(func(x0+h)+func(xn-h))
    do i=3,n-3,2
       integ=integ+func(x0+i*h)
    enddo
 end if
 integ=integ*h

 end subroutine integrate2
!-------------------------!

!----------------!
 function func(x)
!----------------!
 implicit none
 
 real(8) :: epsilon,alpha
 common/funcblock/epsilon,alpha

 real(8) :: func,x

 func=1.d0/(epsilon+x)**alpha

 end function func
!-----------------!








    