""" Exact diagonalization code to find the ground state of 
a 1D quantum Ising model with conservation of parity and momentum."""


import numpy as np
import pylab as pl

def translate(s,N):
    bs = bin(s)[2:].zfill(N)
    return int(bs[1:]+bs[0],2)
        
def checkstate(s,k,N):
    t = s
    for i in range(N):
        t = translate(t,N)
        if t < s:
            return -1
        elif (t == s):
            if (np.mod(k,N/(i+1)) != 0):
                return -1
            else:
                return i+1

def representative(s,N):
    r = s; t = s; l = 0
    for i in range(N):
        t = translate(t,N)
        if (t < r):
            r = t; l = i+1
    return r, l

def flip(s,i,N):
    st = [int(x) for x in bin(s)[2:].zfill(N)]
    st[i] = np.mod(st[i]+1,2)
    st[np.mod(i+1,N)] = np.mod(st[np.mod(i+1,N)]+1,2)
    return int(''.join(str(x) for x in st),2)

def calc_basis(N):
    basis = {}
    invbasis = {}
    for s in range(2**N):
        parity = (-1)**(N-bin(s).count('1'))
        for k in range(-N//2+1,N//2+1):
            R = checkstate(s,k,N)
            if R > 0:
                if basis.has_key((parity,k)):
                    basis[parity,k].append((s,R))
                    invbasis[parity,k][s] = (len(invbasis[parity,k]),R)
                else:
                    basis[parity,k] = [(s,R)]
                    invbasis[parity,k] = {}
                    invbasis[parity,k][s] = (0,R)
                
    return basis, invbasis

def calc_h(N,h):
    basis, invbasis = calc_basis(N)
    H = {}
    for qn in basis:
        M = len(basis[qn])
        H[qn] = np.zeros((M,M),dtype=np.complex)
        a = 0
        for sa, Ra in basis[qn]:
            H[qn][a,a] = h*(-N + 2*bin(sa)[2:].count('1'))
            for i in range(N):
                sb, l = representative(flip(sa,i,N),N)
                if invbasis[qn].has_key(sb):
                    b,Rb = invbasis[qn][sb]
                    k = qn[1]*2*np.pi/Ra
                    H[qn][b,a] += np.exp(-1j*k*l)*np.sqrt(Ra/Rb)
            a += 1
    return H

if __name__ == "__main__": 
    N = 10
    H = calc_h(N,1)
    E = {}
    for qn in H:
        k = qn[1]
        Enew = np.linalg.eigvalsh(H[qn])
        if E.has_key(k):
            E[k] = np.concatenate((E[k],Enew))
        else:
            E[k] = Enew

    for k in E:
        print(k)
        pl.plot(k*np.ones(len(E[k])),np.real(E[k]),'bo')
    pl.ylim([-0.5,0.5])
    pl.xlabel('$k/\\pi$')
    pl.ylabel('$E(k)$')
    pl.show()