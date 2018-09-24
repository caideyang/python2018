# #!/usr/bin/python3
# #@Author:CaiDeyang
# #@Time: 2018/9/6 16:05
#
#
data = [1,3,5,6,7,11,13,15,21,34,45,56,67,76,87,121,134,145,156,176,189]
#
# def func(index,value,L):
#     l = len(L)//2
#     index += l
#     print(l)
#     if l <= 1:
#         return index
#     if db[index] == value:
#         return index
#     elif db[l] < value:
#         return func(index,value,L[index:])
#     else:
#         return func(index,value,L[0:index])
#
# print(func(0,3,db))


def binarySearch(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = (start + end) // 2
        if target > nums[middle]:
            start = middle + 1
        elif target < nums[middle]:
            end = middle - 1
        else:
            return middle
    return  -1

# print(binarySearch(db,76))


start = 0
def index_search(nums,target):
    global start
    end = len(nums)
    if start <= end:
        middle = (start + end) // 2
        print(nums, len(nums), middle)
        if target > nums[middle]:
            start = middle + 1
            index_search(nums[start:end],target)
        elif target < nums[middle]:
            end = middle
            index_search(nums[start:end],target)
        else:
            return middle
    else:
        return "未找到！"

print(index_search(data, 67))