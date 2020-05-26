# -*- coding: utf-8 -*-
"""
Created on Sun May 17 16:30:49 2020

@author: AALAP RANA
"""
import numpy as np
"""
n=3
r=np.zeros((n,n,2))

r_out=np.zeros((n,n,2))
r[0,1]=[1,2]
r[0,2]=[-np.inf,np.inf]

r[1,2]=[3,4]    
r[0,2]=[2,3]
6
r[1,0]=[-r[0][1][1],-r[0][1][0]]
r[2,0]=[-r[0][2][1],-r[0][2][0]]

r[2,1]=[-r[1][2][1],-r[1][2][0]]

"""
"""
n=4 #Quiz question
r=np.zeros((n,n,2))

r_out=np.zeros((n,n,2))
r[0,1]=[30,40]
r[0,2]=[-np.inf,np.inf]
r[0,3]=[-np.inf,np.inf]


r[1,2]=[-np.inf,np.inf]
r[1,3]=[-10,10]

r[2,3]=[5,10]


r[1,0]=[-r[0][1][1],-r[0][1][0]]
r[2,0]=[-r[0][2][1],-r[0][2][0]]
r[3,0]=[-r[0][3][1],-r[0][3][0]]

r[2,1]=[-r[1][2][1],-r[1][2][0]]
r[3,1]=[-r[1][3][1],-r[1][3][0]]

r[3,2]=[-r[2][3][1],-r[2][3][0]]

"""
"""
n=5
r=np.zeros((n,n,2))


r[0,1]=[1,3]# textbook sum 4.9 but r12=[1,3] not r12=[1,2]
r[0,2]=[-np.inf,np.inf]
r[0,3]=[-np.inf,np.inf]
r[0,4]=[6,7]

r[1,0]=[-3,-1]
r[2,0]=[-np.inf,np.inf]
r[3,0]=[-np.inf,np.inf]
r[4,0]=[-7,-6]


r[1,2]=[-np.inf,np.inf]
r[1,3]=[3,4]
r[1,4]=[-np.inf,np.inf]

r[2,1]=[-np.inf,np.inf]
r[3,1]=[-4,-3]
r[4,1]=[-np.inf,np.inf]

r[2,3]=[1,2]
r[2,4]=[4,5]

r[3,2]=[-2,-1]
r[4,2]=[-5,-4]

r[3,4]=[-np.inf,np.inf]
r[4,3]=[-np.inf,np.inf]
"""

n=4
r=np.zeros((n,n,2))


r[0,1]=[20,25]#r12
r[0,2]=[-np.inf,np.inf]#r13
r[0,3]=[0,70]#r14

r[1,0]=[-25,-20]#r21
r[1,2]=[25,35]#r23
r[1,3]=[-np.inf,np.inf]#r24

r[2,0]=[-np.inf,np.inf]#r30
r[2,1]=[-35,-25]#r32
r[2,3]=[10,15]#


r[3,0]=[-70,0]
r[3,1]=[-np.inf,np.inf]
r[3,2]=[-15,-10]



def Check_consistency(r):
    
    for k in range (0,n):
        for i in range(0,n):
            for j in range(0,n):
                if ((i!=k) and (j!=k) and (i<j)):
                    a=r[i][k][0]+r[k][j][0]
                    b=r[i][k][1]+r[k][j][1]
                    d=max(r[i][j][0],a)
                    e=min(r[i][j][1],b)
                    if (r[i][j][1]<d):
                        print("Inconsistent system")
                        print("This system is inconsistent for interation {}".format(k))
                        flag=0
                        return flag
                    else:
                         print("This system is consistent for interation {}".format(k))
   
flag_PC= Check_consistency(r) 

                    

if(flag_PC!=0):
    for k in range (0,n):
        for i in range(0,n):
            for j in range(0,n):
                if ((i!=k) and (j!=k) and (i<j)):
                    a=r[i][k][0]+r[k][j][0]
                    b=r[i][k][1]+r[k][j][1]
                    d=max(r[i][j][0],a)
                    e=min(r[i][j][1],b)
                    r[i][j][0]=d
                    r[i][j][1]=e
                    r[j][i][0]=-e
                    r[j][i][1]=-d
        
        
        print("\n")            
        print("This is the values at the iteration:",k)
        for p in range(n):
            for q in range(n):
                print("r",p+1,q+1,"=", sep='_', end='', flush=True)
                print(r[p][q])



    print("\n")
    print("Element reverse checking:")
    print("\n")
    for p in range(n):
        for q in range(n):
            if ((r[p][q][0]==-r[q][p][1]) and (r[p][q][1]==-r[q][p][0])):
                print("r",p+1,q+1,"=", sep='_', end='', flush=True)
                print("reverse checked")
            else:
                print("reverse is wrong check manually for answer")


    print("\n")
    print("final answer")  
    print("\n")    
    for p in range(n):
        for q in range(n):
            print("r",p+1,q+1,"=", sep='_', end='', flush=True)
            print(r[p][q])
else:
    print("Inconsistent")