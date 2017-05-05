import numpy as np
from numpy import linalg as LA

def mulvec(a,b):
	return np.einsum('ik,k->i',a,b)

# Contextuality research (neutrino)

#                                           MIXING MATRIX

Mixing=[[0 for i in range(0,3)] for j in range(0,3)] # empty 3-dimensional matrix

Mixing[0][0]=np.cos(theta12)*np.cos(theta13)
Mixing[0][1]=np.sin(theta12)*np.cos(theta13)
Mixing[0][2]=np.sin(theta13)

Mixing[1][0]=-np.sin(theta12)*np.cos(theta23)-np.cos(theta12)*np.sin(theta23)*np.sin(theta13)
Mixing[1][1]=-np.cos(theta12)*np.cos(theta23)-np.sin(theta12)*np.sin(theta23)*np.sin(theta13)
Mixing[1][2]= np.sin(theta23)*np.cos(theta13)

Mixing[2][0]=np.sin(theta12)*np.sin(theta23)-np.cos(theta12)*np.cos(theta23)*np.sin(theta13)
Mixing[2][1]=-np.cos(theta12)*np.sin(theta23)-np.sin(theta12)*np.cos(theta23)*np.sin(theta13)
Mixing[2][2]=np.cos(theta13)*np.cos(theta23)

#                                           HAMILTONIAN

# a) Kinetic part of Hamiltonian

Hkin = [[En - deltam12/(4*En), 0], [0, En + deltam12/(4*En)]] 

# b) Potential part of Hamiltonian

Hpot=[[1+math.cos(2*theta),math.sin(2*theta)*cmt.exp(-1j*phi)],[math.sin(2*theta)*cmt.exp(1j*phi),1-math.cos(2*theta)]]

Hpot=V0/2*np.asarray(Hpot)