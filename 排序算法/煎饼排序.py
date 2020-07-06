#煎饼排序
A = [3, 2, 4, 1]
result = []
length = len(A)

while True:
    #判断最大的是否在第一位
    if length == 0  or A == sorted(A):
        break

    # 找到最大值的索引
    index = A[:length].index(max(A[:length]))
    
    # 判断最大值是否在最末尾
    if  index != length:
        # 判断最大值是否在第一位
        if index != 0:
            # 将其颠倒至第一位
            # 颠倒数组A前index个元素
            A[:index+1] = list(reversed(A[:index+1]))
            result.append(index+1)
        # 此时最大的元素已经在第一位了，然后再将最大的元素颠倒到等于他值得位置，比如：4，应该前4个元素颠倒
        temp = A[0]
        A[:temp] = list(reversed(A[:temp]))
        result.append(temp)
    # 然后将排好序的元素剔除在处理范围之内
    length = length - 1

print(result)

