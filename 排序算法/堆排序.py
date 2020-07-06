
def HeapAdjust(lst, parent, lenght):
    # 保留根节点
    temp = lst[parent]
    # 得到左子节点
    child = 2 * parent + 1
    while child < lenght:
        # 判断哪右子节点存在，并且比左子节点大
        if child + 1 < lenght and lst[child] < lst[child+1]:
            # 选定右子节点
            child += 1
        # 如果根节点大于子节点,则说明根节点是堆中最大的数
        if temp > lst[child]:
            break
        # 否则根节点小于子节点，将子节点的值赋给根节点
        lst[parent] = lst[child]
        #选定子节点作为根节点
        parent = child
        child = 2 * parent + 1
    lst[parent] = temp


def heap_Sort(lst):
    # 将堆初始化为最大堆
    for i in range(len(lst) // 2)[::-1]:
        HeapAdjust(lst, i, len(lst))

    for j in range(1, len(lst))[::-1]:
        # 将最大值(也就是第一个，堆顶)与最后一个值进行交换
        lst[0], lst[j] = lst[j], lst[0]

        # 将剩下的堆进行调整
        HeapAdjust(lst, 0, j)



if __name__ == "__main__":
    lst = [50,123,543,187,49,30,0,2,11,100]
    heap_Sort(lst)
    print(lst)

