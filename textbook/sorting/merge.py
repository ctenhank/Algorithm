arr = [7, 5, 9, 14, 7, 7, 3, 1, 6, 2, 4, 8]


def merge_sort(array):
    if len(array) == 1:
        return array

    half = int(len(array) / 2)
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    ret = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1

    while i < len(left):
        ret.append(left[i])
        i += 1

    while j < len(right):
        ret.append(right[j])
        j += 1

    return ret


print(arr)
print(f"Merge sort: {merge_sort(arr)}")
