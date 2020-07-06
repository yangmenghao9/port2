import time
import random
def shell_Sort(lst):
    step = len(lst)
    while step != 1:
        step = step // 2
        for i in range(step,len(lst)):
            temp = lst[i]
            j = i
            while j >= step and lst[j-step] > temp:
                lst[j] = lst[j-step]
                j -= step
            lst[j] = temp

if __name__ == "__main__":
    lst = [8, 5, 6, 9, 2, 1, 3, 4, 7, 0]
    lst = list(range(1000))
    random.shuffle(lst)
    start = time.time()
    shell_Sort(lst)
    end = time.time()
    print(end - start)
    # print(lst)