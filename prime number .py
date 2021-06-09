
# Prime numbers woh numbers hote hai jo sirf 1 aur apne aap se divisible hote hain. 
# Jaise 1. 13 prime hai kyunki 13 sirf 13 aur 1 se perfectly divide hota hai.
#  Aur kisi bhi number se perfectly divide nahi hota. 
# 2. 4 prime nahi hai kyunki 4 apne aap se aur 2 aur 1 se perfectly divide hota hai.
# Prime number ke liye aapko check karna hoga
#  ki woh number kaun kaun se numbers se divisible hai. 
#  Yeh loop chala ke kar sakte ho.


num=int(input("enter a number"))
f=0
i=2
while i<=num/2:
   if num%i==0:
      f=1
      break
   i=i+1
if f==0:      
   print(" it is a prime number")
else:
   print("it is not a prime number")      
    