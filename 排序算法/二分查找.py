def binarySearch(lst, item):
    start_index = 0
    end_index = len(lst) - 1

    while start_index <= end_index:
        mid_index = (end_index + start_index) // 2 
        if  item == ls[mid_index]:
            print("找到元素")
            return [item]
        elif item < lst[mid_index]:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

    print("该数组中未找到该元素")
    return [-1]    

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binarySearch(ls, 3))
