N,K=map(int,(raw_input()).split())
a=[]
c=0
for i in range(0,N):
    a.append((raw_input()))
for j in range(0,len(a)):
    for k in range(j+1,len(a)):
        if(a[j]==a[k]):
            c=c+1
        else:
            c=c
if(c==K):
    print("yes")
else:
    print("no")
