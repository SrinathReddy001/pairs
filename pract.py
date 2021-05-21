l = [1, 2, 3, 1, 2, 3,4,5,4,6,7]
i=0
j=0
c=0
pairs=0
while(i<len(l)):
    x=l[i]
    while(j<len(l)):
        if(x==l[j] and x!=0):
            c+=1
            l[j]=0
        j+=1
    pair=c//2
    pairs+=pair
    c=0
    j=0
    i+=1
print(pairs)