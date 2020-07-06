import time
import random

def merge(left, right):
    i = j = 0
    lst = []
    h = len(left)
    r = len(right)
    while i < h and j < r:
        if left[i] < right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1

    # 如果left还没处理完
    if i < h:
        # 将left处理完
        for k in left[i:]:
            lst.append(k)
    else:
        # 否则将right处理完
        for k in right[j:]:
            lst.append(k)
    return lst

def merge_Sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_Sort(lst[:mid])
    right = merge_Sort(lst[mid:])
    return merge(left, right)

if __name__ == "__main__":
    lst = [8, 5, 6, 9, 2, 1, 3, 4, 7, 0]
    lst = list(range(1000))
    random.shuffle(lst)
    start = time.time()
    lst = merge_Sort(lst)
    end = time.time()
    print(lst)
    print(end - start)
    