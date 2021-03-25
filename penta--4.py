a=input('String: ')
n=len(a) 
a=a+"/0" 
i=0
while i<n:
    f=1
    if i>=n:
        break
    if a[i+1]==a[i]: 
        count=1
        while a[i+1]==a[i]: 
            i=i+1
            if i>=n:
                break
            count+=1 
        print(a[i],end='') 
        print(count,end='')
        f=0
        i+=1
    if(f==1): 
        print(a[i],end='') 
        i+=1
        f=1
        if i>=n:
            break
