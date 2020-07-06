import time
import random
def insert_Sort(lst):
    for i in range(1,len(lst)):
        for j in range(i,0,-1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]


if __name__ == "__main__":
    lst = [8, 5, 6, 9, 2, 1, 3, 4, 7, 0]
    lst = list(range(1000))
    random.shuffle(lst)
    start = time.time()
    insert_Sort(lst)
    end = time.time()
    print(end - start)
    # print(lst)