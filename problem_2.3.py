input_number = int(input('Enter numbers: '))
num = []

for i in range(0, input_number):
    element = int(input('Enter element: '))
    num.append(element)

total = sum(num)
avg = total/input_number
print(round(avg, 2))
