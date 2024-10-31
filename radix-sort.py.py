
def radix_sort(lst):
    if lst == []:
        return []
    max_num = max(lst)
    num_digits = 0
    while max_num > 0:
        max_num /= 10
        num_digits += 1
    for digit in range(num_digits): #this will still work with range(4) instead
        temp = []
        for n in range(0,10):
            for num in range(len(lst)):
                if (lst[num] // pow(10, digit)) % 10 == n:
                    temp.append(lst[num])
        lst = temp
    return lst





# Basic Test Cases
assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]
assert radix_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert radix_sort([4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4]
assert radix_sort([10]) == [10]
assert radix_sort([]) == []
