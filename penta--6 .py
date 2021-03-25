import random
from itertools import permutations
s=[]
s1=[]
j=0
k=1
D=int(input("days: "))
S=int(input("no.of sub: "))
H=int(input("hrs: "))
for i in range(S):
    s1=str(input("subject name: "))
    s.append(s1)
S1=S-H
if(S1<0):
    S1=S1*-1
    for i in range(S1):
        s.append(s[i])
temp = list(permutations(s,H))
l=len(temp)
l1=0
print(l)
if (H>1):
    for i in range(D):
        if(l>6):
            l1+=3
            print("Day",i+1," ",random.sample(temp,k))
        else:
            print("Day",i+1," ",temp[i+l1])
elif (H==1 and S==2):
    while(i<D):
        if(j==0):
            print(s[j])
            j=1
        else:
            print(s[j])
            j=0
        i += 1
else:
    print("")
#logic--2
   #for i in range(D):
        # While(i<H):
           # r=random.sample(s,H)
           #s.append(r)
        #print(s)




#logic--3
#           for i in range(l):
#	while(i<l):
#		a.append(s[i])
#		i += 1
#	l1=len(a)
#	while(l1!=l):
#		l1 += 1
#		a1.append(s[-l1])
#	print(a+a1)
#	a=[]
#	a1=[]
#	l1=0

# output	
#[1, 2, 3, 4, 5]
#[2, 3, 4, 5, 1]
#[3, 4, 5, 2, 1]
#[4, 5, 3, 2, 1]
#[5, 4, 3, 2, 1]

    
