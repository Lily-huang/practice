# -*- codeing:utf-8 -*-

def binary_sort(array):
    if array is None:
        return array
    n = len(array)
    if n == 1:
        return array
    i = 0
    while i < n:
	left = 0
	right = i - 1
	no = array[i]
	while right >= left:
	    m = (left + right) / 2
	    if no < array[m]:
		right = m - 1
	    else:
		left = m + 1
	j = i - 1
	while j >= left:
	    array[j + 1] = array[j]
	    j = j - 1
	array[left] = no
    	i = i + 1
        print(">>>",i,"<<<",array)
    return array

def print_exc(ori,arrays):
    length = len(arrays)
    print(ori,binary_sort(arrays))

if __name__ == "__main__":
    a = [8,9,3,1,6,2,4,11]
    b = [2,44,21,32,22,21,12,8]
    c = [3]
    d = [5,3]
    print_exc(a,a)
    print_exc(b,b)
    print_exc(c,c)
    print_exc(d,d)
