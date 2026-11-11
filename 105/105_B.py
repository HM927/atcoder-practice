def cake(cake_num, dounut_num):

    if 4 * cake_num + 7 * dounut_num > n:
        return -1

    if 4 * cake_num + 7 * dounut_num == n:
        return 1

    cake_num += 1

    a = cake(cake_num, dounut_num)
    b = dounut(cake_num, dounut_num)

    return max(a, b)

def dounut(cake_num, dounut_num):

    if 4 * cake_num + 7 * dounut_num > n:
            return -1

    if 4 * cake_num + 7 * dounut_num == n:
        return 1

    dounut_num += 1

    a = cake(cake_num, dounut_num)
    b = dounut(cake_num, dounut_num)

    return max(a, b)


n = int(input())

a = cake(0, 0)
b = dounut(0, 0)

if a == 1 or b == 1:
     print("Yes")
else:
     print("No")
