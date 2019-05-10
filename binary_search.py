def binary_search(list, item):
    # low和high用于跟踪要在其中查找的部分列表
    low = 0
    high = len(list) - 1

    # 只要范围没有缩小倒只包含一个元素
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        return None

# 以下是函数测试
my_list = [1, 3, 5, 12, 15, 33]

print("元素5在列表中的位置是：" + binary_search(my_list, 5))



