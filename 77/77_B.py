n = int(input())

def binary_search(target):
    left = 0
    right = target + 1
    while right - left > 1:
        mid = (left + right) // 2

        if mid ** 2 <= target:
            left = mid

        elif mid ** 2 > target:
            right = mid

    return left

print(binary_search(n) ** 2)
