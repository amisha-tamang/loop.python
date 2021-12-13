
# 0 4 8
# 4 8 12
# 8 12 16


i=0
count=0
g=0
while i<3:
    j=0
    while j<3:
        print(count,end=" ")
        count=count+4
        if j==0:
            g=count
        j=j+1
    print()
    count=g
    i=i+1