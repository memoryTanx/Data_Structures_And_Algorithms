def bubble_sort(nums):
    """冒泡排序"""
    n = len(nums)
    for c in range(n):
        for i in range(1, n - c):
            if nums[i-1] > nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]


nums = [0, 6,5,7,4,8,3,9,2,0,1]
# bubble_sort(nums)
# print(nums)

def short_bubble_sort(nums):
    """冒泡排序：性能改进，若已经有序，则不在对比"""
    has_changed = True
    n = len(nums)
    while n > 0 and has_changed:
        has_changed = False  # 若全部对比后，没调整顺序（没将 has_change = True），即有序了
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                has_changed = True
                nums[i], nums[i-1] = nums[i-1], nums[i]

        n = n - 1


# short_bubble_sort(nums)
# print(nums)

def selection_sort(nums):
    """选择排序，找最大的值，放在末尾"""
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]

# selection_sort(alist)
# print(alist)

def insertion_sort(alist):
    """插入排序"""
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and alist[position-1] > current_value:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = current_value

# insertion_sort(alist)
# print(alist)

def shell_sort(alist):
    """谢尔排序"""
    sublistcount = len(alist)//2

    while sublistcount > 0:
        for startpostion in range(sublistcount):
            gapInsertionSort(alist, startpostion, sublistcount)

        print(sublistcount, alist)

        sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        current_value = alist[i]
        position = i

        while position >= gap and alist[position-gap] > current_value:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = current_value


def merge_sort(alist):
    """归并排序"""
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


# merge_sort(alist)
# print(alist)


def merge_sort1(lst):
    """归并排序 Pythonic"""

    if len(lst) <= 1:  # 递归结束条件
        return lst

    # 分解问题，并递归调用
    middle = len(lst) // 2
    left = merge_sort1(lst[:middle])
    right = merge_sort1(lst[middle:])

    # 合并左右半部，完成排序
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged

# alist = merge_sort1(alist)
# print(alist)


def quick_sort(alist):
    """快速排序"""
    quick_sort_helper(alist, 0, len(alist) - 1)

def quick_sort_helper(alist, first, last):
    if first < last:
        splitpoin = partition(alist, first, last)

        quick_sort_helper(alist, first, splitpoin-1)
        quick_sort_helper(alist, splitpoin+1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and \
                alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while rightmark >= leftmark and \
                alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True  # 交叉了，就结束
        else:
            # 换位
            alist[leftmark], alist[rightmark] = \
            alist[rightmark], alist[leftmark]

    # 中间值，与
    alist[first], alist[rightmark] = \
    alist[rightmark], alist[first]

    return rightmark
