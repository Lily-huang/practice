# -*- coding:utf-8 -*-

def binary_search(sorted_array, start, num):
    if sorted_array is None:
        return -1
    array_len = len(sorted_array)
    if array_len == 0:
        return -1
    if array_len == 1:
        one = sorted_array[0]
        if one == num:
            return start + 1
        else:
            return -1
    mid = array_len//2
    mid_num = sorted_array[mid]
    if mid_num == num:
        return start + mid
    elif mid_num > num:
        return binary_search(sorted_array[0:mid], start, num)
    else:
        start = start + mid
        return binary_search(sorted_array[mid:len(sorted_array)], start, num)

def print_exc(arr, num):
    print('>>>', num,'<<<', binary_search(arr, 0, num))

if __name__ == "__main__":
    a = [0,2,4,5,6,7,8,11,13]
    print a
    b1 = 3
    b2 = 4
    b3 = 6
    b4 = 1
    b5 = 2
    b6 = 8
    b7 = 10
    print_exc(a,b1)
    print_exc(a,b2)
    print_exc(a,b3)
    print_exc(a,b4)
    print_exc(a,b5)
    print_exc(a,b6)
    print_exc(a,b7)
    print_exc([],4)
