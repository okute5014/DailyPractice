#Write a python program that accept an integer number from user and determines whether it is even or odd.
#EvenOdd.py
i=int(input("Enter an integer number it checks even or odd:")) #6
if(i%2==0):
    print("The number {} is even".format(i))
else:
    print("The number {} is odd".format(i))