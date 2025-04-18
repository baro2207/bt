"""
Viết 1 game Tài xỉu dưa trên nguyên tắc gieo 2 con xúc sắc ngẫu nhiên.
Nếu tổng giá trị của 2 con xúc sắc > 5, gọi là "Tài"
Còn không, gọi là "Xỉu"

Cho người dùng chọn 1 trong 2 trạng thái Tài hoặc Xỉu.
So sánh kết quả.
Hỏi người chơi có tiếp tục không? Nếu có thì chơi tiếp cho dến khi người dùng chọn không.

Mở rộng:
    1. Bắt đầu chơi, cho người dùng 1 số tiền là 100,000. Số tiền cược của mỗi lần chơi
        là 10,000. Sau khi người dùng chọn không chơi tiếp hoặc hết tiền thì ngưng. Sau đó thống kê
        tiền của người chơi, số ván thắng. (có thể cho người dùng chọn số tiền đặt cược)
    2. Cho phép người dùng cược vào số 5 (3 trạng thái thay vì 2 (Tài/Xỉu). Nếu người dùng cược đúng
        thì thắng được 3 lần số tiền cược.
"""
import random

def game_engine(bet):
    is_win = False
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    sum_dice = dice_1 + dice_2

    while True:
        try:
            select = int(input("Hay cho tai (1), xiu (2), hoac so 5 (5): "))
            if select in [1, 2, 5]:
                break
            else:
                print("Lua chon khong hop le")
        except ValueError:
            print("Nhap so hop le!")
    print(f"Dice rolled: {dice_1} + {dice_2} = {sum_dice}")
    if sum_dice > 5:
        if select == 1:
            print("ban thang")
            is_win = True
            return bet, is_win
        else:
            print("ban thua")
            return 0, is_win
    elif sum_dice < 5:
        if select == 2:
            print("ban thang")
            is_win = True
            return bet, is_win
        else:
            print("ban thua")
            return 0, is_win
    elif sum_dice == 5:
        if select == 5:
            print("ban thang gap 3 lan tien cuoc")
            is_win = True
            return bet * 3, is_win
        else:
            print("ban thua")
            return 0, is_win

if __name__ == '__main__':
    no_play = 0
    no_win = 0
    no_lose = 0
    money = 100000
    while money > 0:
        print(f"So tien hien tai: {money} VND")
        try:
            bet = int(input("Nhap so tien ban muon cuoc (>=10000): "))
            if bet < 10000 or bet > money:
                print("So tien cuoc khong du de thuc hien")
                print("Vui long nhap lai")
                continue
        except ValueError:
            print("Vui long nhap so hop le!")
            continue

        no_play += 1
        money -= bet
        win_amount, is_win = game_engine(bet)
        if is_win:
            no_win +=1
            money += win_amount
        else:
            no_lose += 1

        if money < 10000:
            print("\nBan khong du tien de tiep tuc choi")
            break
        response = input("Ban co muon choi lai khong n/N de dung: ").lower()
        if response == 'n':
            break

    print("play counts:", no_play)
    print("Win counts:", no_win)
    print("Lose counts:", no_lose)
    print("money: ", money)