cnt = 0


def recursive_function():
    global cnt
    cnt += 1
    print(f"나는 재귀함수 at {cnt}")
    recursive_function()


recursive_function()
