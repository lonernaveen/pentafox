a=[]
b=[]
i=0
j=0
k=0
c=0
s=int(input("enter sum: "))
n=5
for i in range(5):
      a=int(input())
      b.append(a)
for i in range(5):
    for j in range(i+1,5):
        k=b[i]+b[j]
        if(k==s):
            print(b[i],b[j])
            c +=1
if(c==0):
    print("No Pairs found")

