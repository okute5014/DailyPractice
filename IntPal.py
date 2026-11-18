#write a program to check whether is given integer is palindrome number 
#IntPal.py
i=int(input("Enter a integer number is palindrome: "))
j=i
rev=0
while(i>0):
    d=i%10
    rev=rev*10+d
    i=i//10
if(j==rev):
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")