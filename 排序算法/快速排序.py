import time
import random
def quickSort_part(lst, left, right):
    # 保存基准值
    temp = lst[left]

    while left < right:
        while left < right and temp <= lst[right]: # lst[right]比基准数大
            right -= 1                             # 右指针向左移一位
        lst[left] = lst[right]                     # 否则将lst[right]移到基准数位置
        while left < right and temp >= lst[left]:  # lst[left]比基准数小
            left += 1                              # 左指针向右移一位
        lst[right] = lst[left]                     # 否则将lst[left]移到基准数位置
    # 将基准数填到基准位置
    lst[left] = temp

    # 返回基准指针
    return left
    
def quickSort(lst, left, right):
    if left < right:
        # 获得基准坐标
        mid_index = quickSort_part(lst, left, right)
        #将左边排序
        quickSort(lst, left, mid_index-1)
        #将右边排序
        quickSort(lst, mid_index+1, right)

if __name__ == "__main__":
    lst = [8, 5, 6, 9, 2, 1, 3, 4, 7, 0]
    lst = list(range(1000))
    random.shuffle(lst)
    start = time.time()
    quickSort(lst, 0, len(lst)-1)
    end = time.time()
    print(end - start)
    # print(lst)