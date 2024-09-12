""" iTEBD code to find the ground state of 
the 1D Ising model on an infinite chain.
The results are compared to the exact results. """

import numpy as np
from scipy import integrate
from scipy.linalg import expm 

# First define the parameters of the model / simulation
J=1.0; g=0.5; chi=5; d=2; delta=0.01; N=1000;
G = np.random.rand(2,d,chi,chi);l = np.random.rand(2,chi)

# Generate the two-site time evolution operator
H = np.array( [[J,-g/2,-g/2,0], [-g/2,-J,0,-g/2], [-g/2,0,-J,-g/2], [0,-g/2,-g/2,J]] )
U = np.reshape(expm(-delta*H),(2,2,2,2))

# Perform the imaginary time evolution alternating on A and B bonds
for step in range(0, N):
    A = np.mod(step,2); B = np.mod(step+1,2)

    # Construct theta        
    theta = np.tensordot(np.diag(l[B,:]),G[A,:,:,:],axes=(1,1))
    theta = np.tensordot(theta,np.diag(l[A,:],0),axes=(2,0))
    theta = np.tensordot(theta,G[B,:,:,:],axes=(2,1))
    theta = np.tensordot(theta,np.diag(l[B,:],0),axes=(3,0))
    
    # Apply U
    theta = np.tensordot(theta,U,axes=([1,2],[0,1]))
 
    # SVD
    theta = np.reshape(np.transpose(theta,(2,0,3,1)),(d*chi,d*chi))
    X, Y, Z = np.linalg.svd(theta); Z = Z.T

    # Truncate
    l[A,0:chi]=Y[0:chi]/np.sqrt(sum(Y[0:chi]**2))
    
    X=np.reshape(X[0:d*chi,0:chi],(d,chi,chi))
    G[A,:,:,:]=np.transpose(np.tensordot(np.diag(l[B,:]**(-1)),X,axes=(1,1)),(1,0,2))

    Z=np.transpose(np.reshape(Z[0:d*chi,0:chi],(d,chi,chi)),(0,2,1))
    G[B,:,:,:]=np.tensordot(Z,np.diag(l[B,:]**(-1)),axes=(2,0))

print "E_iTEBD =", -np.log(np.sum(theta**2))/delta/2

f = lambda k,g : -2*np.sqrt(1+g**2-2*g*np.cos(k))/np.pi/2.
E0_exact = integrate.quad(f, 0, np.pi, args=(g,))[0]
print "E_exact =", E0_exact
