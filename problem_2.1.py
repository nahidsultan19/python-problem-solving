# Find the max number of two numbers.

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if(num1 > num2):
    largest = num1
else:
    largest = num2

# print(largest)

# another way
result = max(num1, num2)
print(result)
