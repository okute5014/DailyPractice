#Write a python program that accept two integer numbers and print the greatest number using if-elif-else. 
#GreNum.py
a=int(input("Enter the first integer number: "))
b=int(input("Enter the second integer number: "))
if(a>b):
    print("The {} is the greatest number".format(a))
elif(a<b):
    print("The {} is the greatest number".format(b))
else:
    print("Both a and b numbers are equal")