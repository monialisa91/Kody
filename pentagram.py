import numpy as np
from numpy import linalg as LA

def mulvec(a,b):
	return np.einsum('ik,k->i',a,b)

v1=np.asarray([1,0,0])
v2=(1/np.sqrt(6))*np.asarray([1,2,1])
iloczyn=np.cross(v1,v2)
norma=LA.norm(iloczyn)
iloczyn=iloczyn/norma
cosinus=np.dot(v1,v2)
complet=1-cosinus
sinus=np.sqrt(1-cosinus*cosinus)
xcoord=iloczyn[0]
ycoord=iloczyn[1]
zcoord=iloczyn[2]
Rotation=[[0 for i in range(0,3)] for j in range(0,3)] # empty 3-dimensional matrix

Rotation[0][0]=cosinus+complet*xcoord*xcoord
Rotation[0][1]=xcoord*ycoord*complet-zcoord*sinus
Rotation[0][2]=xcoord*zcoord*complet+ycoord*sinus

Rotation[1][0]=xcoord*ycoord*complet+zcoord*sinus
Rotation[1][1]=cosinus+ycoord*ycoord*complet
Rotation[1][2]=ycoord*zcoord*complet-xcoord*sinus

Rotation[2][0]=xcoord*zcoord*complet-ycoord*sinus
Rotation[2][1]=ycoord*zcoord*complet+xcoord*sinus
Rotation[2][2]=cosinus+zcoord*zcoord*complet

# Special vectors

N=np.sqrt(1+np.cos(np.pi/5))
BigCos=np.cos(2*np.pi/5)
LittleCos=np.cos(np.pi/5)
BigSin=np.sin(2*np.pi/5)
LittleSin=np.sin(np.pi/5)
v1=N*np.asarray([np.sqrt(LittleCos),1,0])
v2=N*np.asarray([np.sqrt(LittleCos),-LittleCos,LittleSin])
v3=N*np.asarray([np.sqrt(LittleCos),BigCos,-BigSin])
v4=N*np.asarray([np.sqrt(LittleCos),-LittleCos,-LittleSin])
v5=N*np.asarray([np.sqrt(LittleCos),BigCos,BigSin])


v1R=mulvec(Rotation,v1)
v2R=mulvec(Rotation,v2)
v3R=mulvec(Rotation,v3)
v4R=mulvec(Rotation,v4)
v5R=mulvec(Rotation,v5)

