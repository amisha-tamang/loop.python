row=4
i=0
while i<=row:
    j=0
    while j<i:
        print(" ",end=" ")
        j=j+1
    k=i
    while k<=row:
        print("*",end=" ")
        k=k+1
    print()
    i=i+1