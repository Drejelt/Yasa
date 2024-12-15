def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def qsort(arr, partition_limit=10):
    def sort_part(first, last):
        if last - first + 1 <= partition_limit:
            insertion_sort(arr, first, last)
            return

        pivot_index = first + (last - first) // 2
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[first] = arr[first], pivot_value

        low = first + 1
        high = last

        while low <= high:
            while low <= high and arr[low] <= pivot_value:
                low += 1
            while low <= high and arr[high] >= pivot_value:
                high -= 1
            if low < high:
                arr[low], arr[high] = arr[high], arr[low]

        arr[first], arr[high] = arr[high], arr[first]

        sort_part(first, high - 1)
        sort_part(high + 1, last)

    sort_part(0, len(arr) - 1)


test_list = [50, 30, 64, 12, 100, 21, 45]
print("Original List:", test_list)

qsort(test_list, 10)
print("Sorted List:", test_list)
