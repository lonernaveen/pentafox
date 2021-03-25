import string
a=[]
d={}
s1=[]
s=tuple(map(int,input("Enter integers seperated by comma: ").split(',')))
l=len(s)
i=0
a=string.ascii_uppercase
a='0'+a
for i in range(27):
    d[i]=a[i]
for i in range(l):
    s1.append(d[s[i]])
print("".join(s1))
