
# CUBE NUMBER


# i=1
# n=30
# while i<=n:
#     j=1
#     while j<=n:
#         print(j**3)
#         j=j+1
#     i=i+1
#     break






n=int(input("enter the number"))
a=0
while n>0:
    a=a+(n%10)*(n%10)*(n%10)
    n=n//10
print("cube is=",a)

   


