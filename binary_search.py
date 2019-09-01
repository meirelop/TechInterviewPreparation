"""
Binary Search algorithm

Run time: O(logn)
"""



def binary_recursive(data, target, high, low):
    if low > high:
        return

    mid_index = (low+high) // 2
    if target == data[mid_index]:
        return mid_index

    elif target < data[mid_index]:
        high = mid_index - 1
        return binary_recursive(data, target, high, low)

    elif target > data[mid_index]:
        low = mid_index + 1
        return binary_recursive(data, target, high, low)



def binary_iterative(data, target, high, low):
    while low < high:
        mid_index = (low+high) // 2
        if target == data[mid_index]:
            return mid_index

        elif target < data[mid_index]:
            high = mid_index - 1

        elif target > data[mid_index]:
            low = mid_index + 1


data = [1,4,5,7,12,16,17,25,37,42]
target = 125

# print(binary_recursive(data, target, len(data) - 1, 0))

# print(binary_iterative(data,target, len(data)-1, 0))