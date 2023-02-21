import sys

N = int(sys.stdin.readline().rstrip())
part = list(map(int, sys.stdin.readline().rstrip().split()))
part.sort()
M = int(sys.stdin.readline().rstrip())
purchase = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(array, value):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if value == array[mid]:
            return mid
        elif value < array[mid]:
            right = mid - 1
        elif value > array[mid]:
            left = mid + 1
    return None


for item in purchase:
    print("yes" if binary_search(part, item) != None else "no")
