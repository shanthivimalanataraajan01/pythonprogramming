n=int(raw_input())
a=list(map(int,(raw_input()).split()))
c=0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if(i<j<k):
                if(a[i]+a[j]==a[k]):
                    c=c+1
print(c) 
