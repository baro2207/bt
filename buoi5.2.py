'''Tạo 1 danh sách (list) ngẫu nhiên N phần tử (N nhập từ bàn phím) có giá trị từ 1 đến 100 sau đó tạo 1 menu cho phép thực hiện các công việc sau:
In ra danh sách vừa tạo.
In đảo ngược danh sách.
Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
In ra vị trí các phần tử là số nguyên tố.
tìm các số duy nhất (không trùng lặp) trong danh sách.
liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
In ra các đoạn con trong danh sách giảm liên tiếp.
'''
import random
from itertools import count


def in_mang(n):
    lst = []
    for i in range(n):
        ran_num = random.randint(1, 100)
        lst.append(ran_num)
    return lst

def is_prime(n):
    if n < 2:
        return False
    for i in range(int(n**0.5)+1):
        if n % i == 0:
            return True

def menu(list):
    print('''
    -----------MENU-----------
1. In ra danh sách vừa tạo.
2. In đảo ngược danh sách.
3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
4. tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
5. đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
6. In ra vị trí các phần tử là số nguyên tố.
7. tìm các số duy nhất (không trùng lặp) trong danh sách.
8. liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
9. In ra các đoạn con trong danh sách giảm liên tiếp.
10. Thoát''')

    while True:
        set = int(input("Hay chon tu 1 den 10: "))
        if set == 10:
            break
        elif set == 1:
            print(list)
        elif set == 2:
            print(list[::-1])
        elif set == 3:
            print(sorted(list))
        elif set == 4:
            max_val = max(list)
            last_pos = len(list) - 1 - list[::-1].index(max_val)
            print(f"Giá trị lớn nhất: {max_val}, vị trí cuối cùng: {last_pos + 1}")
        elif set == 5:
            x = int(input("Nhập giá trị X: "))
            positions = [i for i, val in enumerate(list) if val == x]
            print(f"Số lượng phần tử X: {len(positions)}")
            print(f"Vị trí: {positions}")
        elif set == 6:
            positions = [i for i, val in enumerate(list) if is_prime(val)]
            print(f"Vị trí: {positions}")
        elif set == 7:
            uniq_val = [val for val in list if list.count(val) == 1]
            print(uniq_val)
        elif set == 8:
            counted = {}
            for val in list:
                counted[val] = counted.get(val, 0) + 1
            for k, v in counted.items():
                print(f"{k}: {v} lần")
        elif set == 9:
            print("Các đoạn con giảm liên tiếp:")
            sub = []
            for i in range(len(list)):
                if not sub or list[i] < sub[-1]:
                    sub.append(list[i])
                else:
                    if len(sub) > 1:
                        print(sub)
                    sub = [list[i]]
            if len(sub) > 1:
                print(sub)

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 10.")



if __name__ == '__main__':
    N = int(input("Hay chon N phần tử: "))
    list = in_mang(N).copy()
    menu(list)