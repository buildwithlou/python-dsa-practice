##BUBBLE SORT; walk through the list, compare two neighbors at a time, swap if they're in the wrong order
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([5, 3, 8, 1]))


##SELECTION SORT: find the smallest element in the list, put it at the beginning, then find the next smallest and put it second, repeat
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selection_sort([5, 3, 8, 1]))


##INSERTION SORT: like sorting playing cards in your hand, pick one card at a time and insert it in the right position among the already sorted cards
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(insertion_sort([5, 3, 8, 1]))


##MERGE SORT: split the list in half, sort each half merge them back together
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


print(merge_sort([5, 3, 8, 1]))


##QUICK SORT: pick a pivot element. Put everything smaller on the left, everything bigger on the right.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([5, 3, 8, 1]))

# List: [5, 3, 8, 1, 9, 2]

# Bubble Sort:    compares neighbors, slow but simple
# Selection Sort: finds minimum each pass, slow but simple
# Insertion Sort: builds sorted portion, good for small lists
# Merge Sort:     splits and merges, fast and stable
# Quick Sort:     pivot based, fastest in practice

# When to Use Which
# Bubble Sort        Learning / never in production
# Selection Sort     Learning / very small lists
# Insertion Sort     Almost sorted data, small lists
# Merge Sort         Large data, need guaranteed speed
# Quick Sort         General purpose, most real applications
