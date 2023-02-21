array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


def binary_search_recursive(array, start, end, data):
    mid = int((start + end) / 2)

    if array[mid] == data:
        return mid
    elif array[mid] > data:
        return binary_search_recursive(array, start, mid, data)
    elif array[mid] < data:
        return binary_search_recursive(array, mid + 1, end, data)
    else:
        return None


def bianry_search_iterative(array, data):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = int((left + right) / 2)
        if array[mid] == data:
            return mid
        elif array[mid] > data:
            right = mid - 1
        else:
            left = mid + 1

    return None


idx = binary_search_recursive(array, 0, len(array), 12)
print(f"{idx}: {array[idx]}")

idx = bianry_search_iterative(array, 12)
print(f"{idx}: {array[idx]}")



