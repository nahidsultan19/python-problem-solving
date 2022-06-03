# # class Number:
# # 	def __init__(self, num1, num2, num3):
# # 		self.num1 = num1
# # 		self.num2 = num2
# # 		self.num3 = num3

# # 	def function(self):
# # 		if self.num1 > self.num2 and self.num1>self.num3:
# # 			return self.num1
# # 		elif self.num2 > self.num1 and self.num2 >self.num3:
# # 			return self.num2
# # 		else:
# # 			return self.num3

# # num = Number(20,30,10)
# # print(num.function())

# # class Student:
# # 	def __init__(self, fname,lname):
# # 		self.fname = fname
# # 		self.lname = lname
# # 		self.email = f'{self.fname}{self.lname}@gmail.com'

# # 	def fullname(self):
# # 		return f'{self.fname} {self.lname}'

# # name = Student('Nahid','Sultan')
# # print(name.fullname())


# # ajke amra list dekhbo


# # def Score(nahid, mamun, passed):
# # 		if nahid >= passed and abul >= passed:
# # 			print ('Both Students are passed')
# # 		elif nahid >= passed or mamun >= passed:
# # 			print ('One student is passed')

# # 			if nahid >= mamun:
# # 				print (f'And it is Nahid with {nahid} Point ')
# # 			else:
# # 				print (f'And it is Abul with {mamun}Point')
# # 		else:
# # 			print('Both Students are failed')


# # Score(20, 50, 50)

# # class Bio:
# # 	def __init__(self, name, age):
# # 		self.name = name
# # 		self.age =age

# # 	def show(self):
# # 		return f'My name is {self.name} and age is {self.age}'

# # myname = Bio('Nahid Sultan', 29)
# # print(myname.show())


# # name = ['nahid','keya','shiren','Ifty','another']
# # one = 'Ifty'
# # for n in name:
# # 	if n in one:
# # 		print(f'You want to find out {one}?')
# # 		break
# # 	else:
# # 		print('You do not have')

# # print("---------------------------------------")

# # numbers=[20,19,10,9,45,62]
# # print(f'Largest number is {max(numbers)}')

# # tupple

# # tpl = ('nahid', 'sultan', 'keya')
# # for t in tpl:
# #     print('Tuple', t)
# # lst= list(tpl)
# # lst.append('shiren')
# # print(lst)

# # print('--------------------------------------')

# # list
# # names = ['Bangladesh', 'india','china']
# # print(names)
# # names.append('Canada')
# # print(names)
# # names.remove('india')
# # print(names)
# # names.sort()
# # print(names)
# # names.insert(2,'Finland')
# # print(names)

# # print('-----------------------------------------')

# # set
# # num = {1,2,3,45,6,7}
# # num2 = set([4,5,6,7])
# # print(len(num))

# # num3 = set()
# # num3.add(2)
# # print(num3)
# # num.remove(45)
# # print(num)

# # print(num | num2 )
# # print(num & num2)
# # print(num - num2 )

# # print(num.intersection(num2))
# # print(num.union(num2))
# # print(num.difference(num2))

# # print('--------------------------')

# # dictionary

# # country = {'Bangladesh': 'Dhaka', 'India': 'Mombai',
# #            'Pakistan': 'Islamabad', 'China': 'Beijing'}

# # country['Bangladesh'] = 'Rajshahi'
# # print(country['Bangladesh'])
# # print(country)

# from itertools import count
# from cv2 import dct


# student = {'name': 'abul', 'age': 24, 'courses': ['Python', 'JavaScript']}

# # student['name'] ='Nahid'
# # student['phone'] ='000000'

# # del student['courses']
# # for key, value in student.items():
# #         print(key,value)


# # print(student)
# # counts = dict()
# # names= ['MacbookPro', 'MackbookAir', 'Lenovo', 'Dell', 'Dell']
# # for name in names:
# #     if name in counts:
# #         counts[name] +=1
# #     else:
# #         counts[name] =1

# # print(counts)

# """ numbers = []

# for num in range(100):
#     numbers.append(num)

# def largestNum(number):
#     largest = number[0]
#     secLarge = number[0]
#     for i in range(len(number)):
#         if number[i] > largest:
#             secLarge = largest
#             largest = number[i]
#         elif number[i] > secLarge:
#             secLarge = number[i]
#     print(secLarge)


# largestNum(numbers) """

# text = 'my name is nahid sultan, i am from bangladesh, i am a software engineer.'

# count = 0

# for line in text:
#     count += 1
# # print(count)

# int_text = int(input('Give me an integer number: '))


# float_text = float(input('Give me a float number: '))

# result = int_text * float_text
# print(result)

# x = 'abcdef'
# i = 'a'
# while i in x[:-1]:
#     # print(i, end=' ')

# print('The {} side {1} {2}'.format('bright', 'of', 'life'))
import re
x = ['ab', 'cd']
# print(list(map(len, x)))
# print(list(map(lambda x: len(x), x)))


# class hello:
#     def __init__(self, a='welcome to'):
#         self.a = a

#     def welcome(self, x):
#         print(self.a + x)


# h = hello()
# h.welcome('Turing')


t = '%(a)s %(b)s%(c)s'
# print(t % dict(a='welcome', b='to', c='turing'))
# print([i.lower() for i in 'TURING'])


def add(c, k):
    c.test = c.test+1
    k = k+1


class Plus:
    def __init__(self):
        self.test = 0


def main():
    p = Plus()
    index = 0

    for i in range(0, 25):
        add(p, index)
    print('p.test=', p.test)
    print('index=', index)


main()

# print('Welcome to TURING'.capitalize())

# f = None
# for i in range(5):
#     with open('app.log', 'w') as f:
#         if i > 2:
#             break

# print(f.closed)

a = [1, 2, 3, 4]
b = [sum(a[0:x+1])for x in range(0, len(a))]
# print(b)

# list1 = [1, 2, 6, 12]
# list2 = [12, 6, 2, 1]
# print(list1 == list2)
# print(set(list1) == set(list2))

arr1 = [1, 2, 3, 4, 5]
arr2 = arr1
arr2[0] = 0
# print(arr1)


def liSkills(val, list=[]):
    list.append(val)
    return list


list1 = liSkills('NodeJS')
list2 = liSkills('Java', [])
list3 = liSkills('ReactJS')

# print('%s' % list1)
# print('%s' % list2)
# print('%s' % list3)

data = [1, 2, 3]


def icnr(x):
    return x+1


# print(list(map(icnr, data)))

def f(x, I=[]):
    for i in range(x):
        I.appned(i*i)

    # print(I)


# f(2)
# f(3, [3, 2, 1])
# f(3)

inp = ['nodejs', 'reactjs', 'vuejs']
print(inp)

for i in inp:
    inp.append(i.upper())

# print(inp)

Y = [2, 5J, 6]
Y.sort()
print(Y)

result = re.findall('welcome to turing', 'Welcome', 1)
print(result)
