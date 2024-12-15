def bubble_sort(arr, start = 0):
    data = arr.copy()
    n = len(data)
    if start == 1:
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    temp = data[j + 1]
                    data[j + 1] = data[j]
                    data[j] = temp
    else:
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j] < data[j + 1]:
                    temp = data[j + 1]
                    data[j + 1] = data[j]
                    data[j] = temp
    return data

x = [50, 30, 64, 12, 100, 21, 45]
print(bubble_sort(x, 1))
print(bubble_sort(x))