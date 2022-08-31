def thrive(n):
    if n % 15 == 0:
        print('thrive', end=' ')
    elif n % 3 != 0 and n % 5 != 0:
        print('neither', end=' ')
    elif n % 3 == 0:
        print('three', end=' ')
    elif n % 5 == 0:
        print('five', end=' ')


thrive(35)
thrive(56)
thrive(15)
thrive(39)
