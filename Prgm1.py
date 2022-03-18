#  Write a while loop that adds all the numbers up to 100 (inclusive)

number = int(input("Enter the limit:"))
sum = 0
i = 1
while(i <= number):
    sum = sum+i
    i=i+1
print("Sum of the numbers upto 100 is", sum)
