num=int(input("enter the number: "))
a=num
sum=0
while a>0:
    b=a%10
    sum+=b
    a=a//10
a+=1
if num%sum==0:
    print(num,"harsad number")
else:
    print(num)