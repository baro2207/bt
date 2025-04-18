import numbers
import random


def ex01():
    for i in range(1, 11):
        print(i)
def ex02():
    num = int(input())
    sum = int(0)
    for i in range(1, num + 1):
        sum += i
    print(sum)
def ex03():
    num = int(input())
    sum_even = int(0)
    sum_odd = int(0)
    for i in range(1, num + 1):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    print("sum of even: ", sum_even)
    print("sum of odd: ", sum_odd)
def ex04():
    str = input()
    total = int(0)
    for char in str:
        total +=  1
    print(total)
def ex05():
    sentence = input("nhap cau: ")
    words = sentence.split(' ')
    word_count = len(words)
    print(word_count)
def ex06():
    num = random.randint(1, 100)
    print("let's choose the level of game")
    selection = int(input("1 for easy(10 times)\n2 for medium (6 time)\n3 for hard(4 times)\n"))
    if selection == 1:
        for i in range(10):
            guess_num = int(input("guess a num from 1 to 100: "))
            if num == guess_num:
                print(f"congrats, you guessed it after {i+1} times")
                break
            else:
                if num > guess_num:
                    print(f"wrong guess, your guess {guess_num} is less than the number computer guess. you have {10-i} left")
                if num < guess_num:
                    print(f"wrong guess, your guess {guess_num} is greater than the number computer guess. you have {10-i} left")
            print("you lose")
    if selection == 2:
        for i in range(6):
            guess_num = int(input("guess a num from 1 to 100: "))
            if num == guess_num:
                print(f"congrats, you guessed it after {i+1} times")
                break
            else:
                if num > guess_num:
                    print(f"wrong guess, your guess {guess_num} is less than the number computer guess. you have {6-i} left")
                if num < guess_num:
                    print(f"wrong guess, your guess {guess_num} is greater than the number computer guess. you have {6-i} left")
            print("you lose")
    if selection == 3:
        for i in range(4):
            guess_num = int(input("guess a num from 1 to 100: "))
            if num == guess_num:
                print(f"congrats, you guessed it after {i+1} times")
                break
            else:
                if num > guess_num:
                    print(f"wrong guess, your guess {guess_num} is less than the number computer guess. you have {4-i} left")
                if num < guess_num:
                    print(f"wrong guess, your guess {guess_num} is greater than the number computer guess. you have {4-i} left")
            print("you lose")
ex06()
