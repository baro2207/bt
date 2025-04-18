import random
def ex01():
    age = int(input())
    if age >= 18:
        print("The person is  eligible for voting")
    else:
        print("The person is not eligible for voting")
def ex02():
    num = int(input())
    if num % 2 == 0:
        print(num, 'is even')
    else:
        print(num, 'is odd')
def ex03():
    num = int(input())
    print("num is divisible by 7") if num % 7 == 0 else print("num is not divisible by 7")
def ex04():
    num = int(input())
    print("is divisible by 3") if (num % 10) % 3 == 0 else print("is not divisible by 3")
def ex05():
    num_guess = int(input())
    num = random.randint(1, 10)
    if num == num_guess:
        print("that's the right number")
    else:
        print("that's the wrong number", num)
def ex06():
    num = int(input())
    if num == 1:
        print("Sunday")
    elif num == 2:
        print("Monday")
    elif num == 3:
        print("Tuesday")
    elif num == 4:
        print("Wednesday")
    elif num == 5:
        print("Thursday")
    elif num == 6:
        print("Friday")
    elif num == 7:
        print("Saturday")
