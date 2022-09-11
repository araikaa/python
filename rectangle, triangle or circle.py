import math
print('1-rectangle, 2-triangle, 3-circle')
figure = input('Choose a figure: ')
if figure == '1':
    print('The lengths of the sides of the rectangle:')
    a = float(input('a = '))
    b = float(input('b = '))
    print('Square:', (a * b))
elif figure == '2':
    print('Triangle side lengths:')
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('Square:', s)
elif figure == '3':
    r = float(input('Circle radius R = '))
    print('Square:',(math.pi * r ** 2))
else:
    print('Input Error')
