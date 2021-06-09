


# ARMSTRONG NUMBER


x=int(input("enter the number"))
orig=x
sum=0
while x>0:
    sum=sum+(x%10)*(x%10)*(x%10)
    x=x//10
if orig==sum:
    print("it armtrong no") 
else:
    print("it is not armstrong no")       




    # an armstrong number is a number each that the sum of its rigths raised
    # to the thrid power is equal to the number itself.
    # FOR EXAMPLE:- 371 is an armstrong number.
    







