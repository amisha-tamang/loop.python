


# STRONG NUMBER
  


num=int(input("enter the number"))
i=1
d=0
while num>i:
    a=num%10
    b=(num//10)%10
    c=(num//10)//10
    d=a+b+c
    if d%10==0:
        print(num,"is strong number")
    else:
        print(num,"is not stong number")    
    i=i+num    





