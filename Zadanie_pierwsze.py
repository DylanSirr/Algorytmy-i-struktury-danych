def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def shell_sort(arr):
    propper_array = arr[:]
    k = 0
    shell_gaps = []
    shell_gap = 1
    while shell_gap < len(arr):
        shell_gaps.append(shell_gap)
        shell_gap = 4**(k+1) + 3*2**k + 1
        k += 1
    shell_gaps.reverse()
    
    for gap in shell_gaps:
        temp_array = []
        indices = list(range(0, len(arr), gap))
        for i in indices:
            temp_array.append(propper_array[i])
        temp_array = insertion_sort(temp_array)
        for i in indices:
            propper_array[i] = temp_array.pop(0)
    
    return propper_array

def selection_sort(arr):
    n = len(arr)
    for j in range(n-1):
        min = j
        for i in range(j+1,n):
            if arr[i]<arr[min]:
                min = i
        arr[j], arr[min]=arr[min], arr[j]
    return arr 

# print([4,56,7,3,2,2,5,7])
# print(selection_sort([4,56,7,3,2,2,5,7]))

