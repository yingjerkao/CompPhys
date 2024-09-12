""" Calculation of dynamical properties using the Lanczos method: 
Spectral function A(k,w) of the fermionic tV model """

import pylab as pl
import numpy as np
import scipy.sparse as sparse
import scipy.sparse.linalg.eigen.arpack as arp

def c_operators(L):
	""" Returns the fermionic annihilation operators c"""
	sp = sparse.csr_matrix(np.array([[0.,1.],[0.,0.]]))
	sz = sparse.csr_matrix(np.array([[1.,0.],[0.,-1.]]))
	
	c_list = []
	for i_site in range(L):
		if i_site==0:
			X=sp
		else:            
			X=sz
            
		for j_site in range(1,L): 
			if i_site==j_site:
				X=sparse.kron(X,sp, 'csr')
			else:
				if j_site < i_site:
					X=sparse.kron(X, sz, 'csr')
				else:
					X=sparse.kron(X, sparse.csr_matrix(np.eye(2)), 'csr')
		
		c_list.append(X)
    
	return c_list

def gen_hamiltonian(c_list,L): 
	"""" Generates the Hamiltonian """    
	H_t = sparse.csr_matrix((2**L,2**L))
	H_V = sparse.csr_matrix((2**L,2**L))   

	for i in range(L):
		H_t = H_t + c_list[i].T*c_list[np.mod(i+1,L)] + (c_list[i].T*c_list[np.mod(i+1,L)]).T
		H_V = H_V + c_list[i].T*c_list[i]*c_list[np.mod(i+1,L)].T*c_list[np.mod(i+1,L)]
		
	return H_t,H_V
	
def lanczos(A, psi, N): 
	""" Simple Lanczos algorithm returning the elements of the tridiagonal matrix """
	   
	dim=A.shape[0]

    # Lanczos I
	q0 = np.zeros((dim,1),dtype=psi[0].dtype)    
	q1 = psi/np.linalg.norm(psi)

	a=[]
	b=[]
	b.append(np.linalg.norm(psi))
	beta = 0.0
	for k in range(N):
		v = A*q1 - beta*q0
      
		alpha = np.dot(np.conj(q1.T),v)[0,0]
		v = v - alpha*q1
		beta = np.linalg.norm(v)
        
		q0 = q1 
		q1 = v/beta
        
		a.append(alpha)
		if k < N-1:
			b.append(beta)
	b.append(0)		
	return np.array(a),np.array(b)

def continued_fraction(a,b,z):
	""" Continuous fraction """
	
	N=a.shape[0]
	g_previous=0

	for c in range(N-1,-1,-1):
		g=1./(z+a[c]-(abs(b[c+1])**2)*g_previous)
		g_previous=g

	g=g_previous*b[0]**2
	return(g)
    

if __name__ == "__main__": 
	# Set parameters here
	L= 	14							    # System size
	V = 0.0								# Transverse field	
	w_list = np.arange(-3,3,0.025)		# Range of energies
	eta = 0.025							# Broadening
	N_lanczos = 20						# Lanczos steps
	
	# Get ground state
	c_list = c_operators(L)
	H_t, H_V = gen_hamiltonian(c_list,L)
	
	H = -H_t + V*H_V
	E0,v = arp.eigsh(H,k=1,which='SA')
	E0 = E0.item()
	
	# Get spectrum
	A_kw = [[],[]]
	k_list = 2*np.pi*np.arange(-L/2,L/2+1)/L
	
	s = 0.
	for k in k_list:
		print k
		ck = sparse.csr_matrix((2**L,2**L))		
		for x in np.arange(0,L):
			ck = ck + np.exp(1j*x*k)*c_list[x]/L
		
		# Get the "hole part"
		psi0 = np.matrix(ck*v)	
		W0 = np.linalg.norm(psi0)**2/np.pi
		a,b = lanczos(H,psi0/np.linalg.norm(psi0),N_lanczos)	
		
		A_w_list = []	
		for w in w_list:
			A_w_list.append(-W0*np.imag(continued_fraction(a,b, w + eta*1j - E0)))		
		if k < np.pi:
			s += np.trapz(A_w_list, x=w_list)    		
		A_kw[0].append(A_w_list)
		
		# Get the "electron part"
		psi0 = np.matrix(ck.transpose().conjugate()*v)	
		W0 = np.linalg.norm(psi0)**2/np.pi
		a,b = lanczos(H,psi0/np.linalg.norm(psi0),N_lanczos)
				
		A_w_list = []	
		for w in w_list:
			A_w_list.append(-W0*np.imag(continued_fraction(-a,b, w + eta*1j + E0)))		
		if k < np.pi:		
			s += np.trapz(A_w_list, x=w_list)    
		A_kw[1].append(A_w_list)
		
	print "Sum rule:", s
	
	# Plot the results"
	pl.figure(figsize=(4, 6))

	pl.subplot(211)
	im = pl.imshow(np.array(A_kw[0]).T[::-1,:],
					aspect='auto', 
					extent=(k_list[0],k_list[-1],w_list[0], w_list[-1]),
					cmap='gist_heat_r')
	pl.plot(k_list,-2*np.cos(k_list),'wo')		
	pl.ylabel('$\\omega$')
		
	pl.subplot(212)
	im = pl.imshow(np.array(A_kw[1]).T[::-1,:],
					aspect='auto', 
					extent=(k_list[0],k_list[-1],w_list[0], w_list[-1]),
					cmap='gist_heat_r')
	pl.plot(k_list,-2*np.cos(k_list),'wo')	
	pl.ylabel('$\\omega$')
	pl.xlabel('$k$')
	
	pl.show()


