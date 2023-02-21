arr = [7, 5, 9, 14, 3, 1, 6, 2, 4, 8]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
    return arr


print(arr)
print(f"Insertion sort: {insertion_sort(arr)}")
