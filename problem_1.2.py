""" Take two numbers from the users. 
Calculate the result of second number power of the first number. """

from unittest import result


num = int(input('ENter your number: '))
power_num = int(input('Enter your power number: '))

# result = num ** power_num
# print(result)

result = pow(num, power_num)
print(result)
