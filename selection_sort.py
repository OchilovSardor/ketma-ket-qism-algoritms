# Sorting from biggest to smallest


arr = [145, 45, 245, 22, 30]


def find_Biggest_arr(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# print(find_Biggest_arr(arr))

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_Biggest_arr(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort(arr))