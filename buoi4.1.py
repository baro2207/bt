import random
def game_engine(count):
    is_win = False
    ran_num = random.randint(1,100)
    for i in range(count):
        guess_num = int(input("Choose num from 1 to 100: "))
        if guess_num == ran_num:
            print(f"that right, you guess correct num after {i+1} times")
            is_win = True
            break
        else:
            if guess_num > ran_num:
                print("your number is greater than computer num")
            else:
                print("your number is less than computer num")
    print(f"the correct num is {ran_num}")
    return is_win

def choose_level():
    print("Choose difficulty")
    print("1 for easy(10 times) \n 2 for medium(6 times) \n 3 hard(4 times)")
    level = 1
    while True:
        game_level = int(input("Choose: "))
        if 1 <= level <=3:
            break
        else:
            print("please choose again!")
    return 10 if level == 1 else 6 if level == 2 else 4


if __name__ == '__main__':
    no_play = 0
    no_win = 0
    while True:
        no_play +=1
        level_game = choose_level()
        if game_engine(level_game):
            no_win += 1

        response = input("Do you want to play again? n/N to stop").lower()
        if response == 'n':
            break
    print("play counts:", no_play)
    print("Win counts:", no_win)

