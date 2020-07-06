def bubbel_Sort(lst):
    for i in range(len(lst)):
        exchange = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                exchange = True
        if not exchange:
            break

if __name__ == "__main__":
    lst = [8, 5, 6, 9, 2, 1, 3, 4, 7, 0]
    bubbel_Sort(lst)
    print(lst)