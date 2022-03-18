# Write a python program to check given number is prime or not

number = int(input("Enter a number:"))
flag = False
if(number>1):
    for i in range(2,number):
        if(number%2==0):
            flag = True
            break
if flag:
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")