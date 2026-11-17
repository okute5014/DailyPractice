#Write a program that accept positive integer from the user and counts how many digits its contains.
#PosInt.py
n=int(input("Enter a positive integer number: "))
count=0
while(n>0):
    count+=1
    n=n//10
print("The given number contains {} digits".format(count))