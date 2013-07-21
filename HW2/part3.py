def partition(arr):
    pivot = arr[0]
    i = 1

    for j in range(1, len(arr)):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    pos = i-1
    arr[0], arr[pos] = arr[pos], arr[0]
    return pos

def quick_sort(arr):
    global count
    if len(arr) <= 1:
        return arr
    count += len(arr)-1
    
    #choose pivot
    if len(arr)%2 == 0:
        ordset = [arr[0],arr[len(arr)/2 - 1], arr[-1]]
    else:
        ordset = [arr[0],arr[len(arr)/2], arr[-1]]
    ordset.sort()
    p = arr.index(ordset[1])
    arr[0], arr[p] = arr[p], arr[0]

    pivot = partition(arr)
    return quick_sort(arr[:pivot]) + [arr[pivot]] + quick_sort(arr[pivot+1:])

count = 0
with open('QuickSort.txt', 'r') as f:
    quick_sort([int(l) for l in f])
print count
