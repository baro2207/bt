
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import math
from operator import truediv

def ex01():
    b = float(input())
    h = float(input())
    S = 0.5 * b * h
    print(S)
def ex02():
    a = float(input())
    b = float(input())
    c = float(input())
    perimeter = a + b +c
    print(perimeter)

def ex03():
    length = float(input())
    width = float(input())
    area = length * width
    perimeter = 2 * (length + width)
    print("area = "+ str(area))
    print("perimeter = " + str(perimeter))
def ex04():
    r = int(input())
    pi = 3.14
    S = r * pi * r
    P = 2 * pi * r
    print(f"area = {S}")
    print(f"circumference = {P}")
def ex05():
    x = int(input())
    y = 2*x -2
    print(y)

def ex06():
    x1, x2 = 2, 4
    y1, y2 = 6, 10
    slope = (y2-y1) / (x2 - x1)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"Slope: {slope}")
    print(f"Euclidean Distance: {distance}")
def ex08():
    for x in range(-10, 10):
        y = x ** 2 + 6 * x + 9
        if y == 0:
            print(f"x = {x}")
def ex09():
    print(len("python")!=len("dragon"))
def ex10():
    if 'on' in 'python' and 'dragon':
        return True
    return False

def ex11():
    sentence = 'jargon not dragon'
    if 'jargon' in sentence: return True
    return False
def ex13():
    num = len('python')
    float_num = float(num)
    string_num = str(float_num)
    print(type(string_num))
def ex14():
    num = int(input())
    if num % 2 == 0:
        print(num, 'is even')
    else:
        print(num, 'is odd')
def ex15():
    hours = float(input())
    rate = float(input())
    pay = float(hours * rate)
    print(pay)
