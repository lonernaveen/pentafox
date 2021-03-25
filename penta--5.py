s=input("First string: ")
s1=input("Second string: ")
a=[]
a1=[]
for i in s:
    a.append(i)
for i in s1:
    a1.append(i)
l=min(len(a),len(a1))
q=[]
for i in range(l):
    for j in range(l):
        if(a[i]==a1[j]):
            q.append(a[i])
for i in range(len(q)):
    a.remove(q[i])
    a1.remove(q[i])
i=''.join(a)+''.join(a1)
print(i)
