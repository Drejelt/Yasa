from functools import cache

#O(log n)
def binary_search(some_list, value, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    if some_list[mid] == value:
        return mid
    elif some_list[mid] < value:
        return binary_search(some_list, value, mid + 1, right)
    else:
        return binary_search(some_list, value, left, mid - 1)

@cache
def fibonacci(n):
    global call_counter
    call_counter += 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev = fibonacci(n - 1)
        pre_prev = fibonacci(n - 2)
        return prev + pre_prev

#O(log n)
def fibonacci_search(arr, x):
    m = 0
    while fibonacci(m) < len(arr):
        m += 1
    offset = -1
    while fibonacci(m) > 1:
        i = min(offset + fibonacci(m - 2), len(arr) - 1)
        print('Current Element:', arr[i])
        if x > arr[i]:
            m -= 1
            offset = i
        elif x < arr[i]:
            m -= 2
        else:
            return i
    if fibonacci(m - 1) and arr[offset + 1] == x:
        return offset + 1
    return -1


if __name__ == "__main__":
    call_counter = 0
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    x = 85
    result = fibonacci_search(arr, x)
    if result != -1:
        print(f'Number found at index: {result}')
    else:
        print('Number not found in array.')
