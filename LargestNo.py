#write a program that accept n integer form the user,store them in list and finds the largest number from the list.
#LargestNo.py
n = int(input("Enter the number of elements: "))
num=[]
for i in range(n):
    ele = int(input("Enter element {}: ".format(i+1)))
    num.append(ele)
largest = num[0]
for i in range(1, n):
    if num[i] > largest:
        largest = num[i]
print("The largest number is:", largest)