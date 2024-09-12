""" Exact diagonalization code to find the ground state of 
a 1D quantum Ising model."""

import scipy.sparse as sparse 
import numpy as np 
import scipy.sparse.linalg.eigen.arpack as arp
import pylab as pl

def gen_spin_operators(L): 
	"""" Returns the spin operators sigma_x and sigma_z for L sites """
	sx = sparse.csr_matrix(np.array([[0.,1.],[1.,0.]]))
	sz = sparse.csr_matrix(np.array([[1.,0.],[0.,-1.]]))
	    
	d = 2
	sx_list = []
	sz_list = []

	for i_site in range(L): 
		if i_site==0: 
			X=sx
			Z=sz 
		else: 
			X= sparse.csr_matrix(np.eye(d)) 
			Z= sparse.csr_matrix(np.eye(d))
            
		for j_site in range(1,L): 
			if j_site==i_site: 
				X=sparse.kron(X,sx, 'csr')
				Z=sparse.kron(Z,sz, 'csr') 
			else: 
				X=sparse.kron(X,np.eye(d),'csr') 
				Z=sparse.kron(Z,np.eye(d),'csr') 
		sx_list.append(X)
		sz_list.append(Z) 
		
	return sx_list,sz_list 

def gen_hamiltonian(sx_list,sz_list,L): 
	"""" Generates the Hamiltonian """    
	H_zz = sparse.csr_matrix((2**L,2**L))
	H_x = sparse.csr_matrix((2**L,2**L))       
	    
	for i in range(L):
		H_zz = H_zz + sz_list[i]*sz_list[np.mod(i+1,L)]
		H_x = H_x + sx_list[i]
     
	return H_zz, H_x 
	
if __name__ == "__main__": 
	# Set parameters here
	L_list = [6,8,10,12]
	g_list = np.arange(0,2,0.1)
	
	for L in L_list:
		sx_list,sz_list  = gen_spin_operators(L)
		H_zz, H_x = gen_hamiltonian(sx_list,sz_list,L)
	
		m_list = []
		for g in g_list:
			H = -H_zz + g*H_x
			e,v = arp.eigsh(H,k=1,which='SA',return_eigenvectors=True)
			m_list.append(np.dot(v.T,sz_list[0]*sz_list[L/2]*v).item())
	
		pl.plot(g_list,m_list)
	
	pl.xlabel("$g$")
	pl.ylabel("$\\langle \\sigma_z(0)\\sigma_z(L/2) \\rangle$")
	pl.show()
	
		
		
		
		
		
