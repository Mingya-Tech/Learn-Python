def binary_search(list, item):
    # 二分查找函数
    # low和high用于跟踪要在其中查找的部分列表
    low = 0
    high = len(list) - 1

    # 只要范围没有缩小倒只包含一个元素
    while low <= high:
        # 就检查中间的元素，注意类型转换
        mid = int((low + high) / 2)
        guess = list[mid]  # 把中间值作为猜的数字
        if guess == item:  # 猜的数和给出的数一样
            return mid
        if guess > item:  # 猜的数字大了
            high = mid - 1
        else:  # 猜的数小了
            low = mid + 1  # 没有指定的元素
        return None

# 以下是测试
my_list = [1, 3, 5, 12, 15, 33]

print("元素5在列表中的位置是：" + binary_search(my_list, 5))