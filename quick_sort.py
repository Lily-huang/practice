# -*- coding:utf-8 -*-

def quick_sort(ori_array, left, right):
    if left < right:
        key = ori_array[left]
	low = left
	high = right
	while low < high:
	    while low < high and ori_array[high] >= key:
		high = high - 1
	    ori_array[low] = ori_array[high]
	    while low < high and ori_array[low] < key:
		low = low + 1
	    ori_array[high] = ori_array[low]
	ori_array[low] = key
	quick_sort(ori_array, left, low-1)
	quick_sort(ori_array, low +1, right)
    return ori_array

def print_exc(ori,arrays):
    length = len(arrays)
    print(ori,quick_sort(arrays,0,length-1))

if __name__ == "__main__":
    a = [8,9,3,1,6,2,4,11]
    b = [2,44,21,32,22,21,12,8]
    c = [3]
    d = [5,3]
    print_exc(a,a)
    print_exc(b,b)
    print_exc(c,c)
    print_exc(d,d)
