""" Swap two variables.

To swap two variables: the value of the first variable will become the value of the second variable. 
On the other hand, the value of the second variable will become the value of the first variable.
 """
a = 5
b = 7
print('a,b', a, b)

# swap
temp = a
a = b
b = temp
print('a,b', a, b)

# another way
x = 3
y = 4

# swap
x, y = y, x
print('x,y', x, y)
