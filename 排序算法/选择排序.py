def select_Sort(lst):
    for i in range(len(lst)):
        # 遍历一次找到最大的数
        for j in range(len(lst)-i):
            if j == 0:
                max = 0
            else:
                if lst[max] < lst[j]:
                    max = j
        # 将最大的跟最末尾的元素交换
        lst[len(lst)-i-1], lst[max] = lst[max], lst[len(lst)-i-1]


if __name__ == "__main__":
    lst = [8, 5, 6, 9, 2, 1, 3, 4, 7, 0]
    select_Sort(lst)
    print(lst)
