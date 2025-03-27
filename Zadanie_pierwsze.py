import sys
import random

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
        min_idx = j
        for i in range(j+1, n):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[j], arr[min_idx] = arr[min_idx], arr[j]
    return arr 

def heapify(arr, n, i):
    max_idx = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[max_idx]:
        max_idx = left
    if right < n and arr[right] > arr[max_idx]:
        max_idx = right
    if max_idx != i:
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        heapify(arr, n, max_idx)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def quick_sort_left_pivot(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort_left_pivot(left) + middle + quick_sort_left_pivot(right)

def quick_sort_random_pivot(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort_random_pivot(left) + middle + quick_sort_random_pivot(right)

# Mapowanie numeru algorytmu na funkcję
algorithm_mapping = {
    "1": insertion_sort,
    "2": shell_sort,
    "3": selection_sort,
    "4": heap_sort,
    "5": quick_sort_left_pivot,
    "6": quick_sort_random_pivot
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python3 Zadanie_pierwsze.py --algorithm <numer_algorytmu>")
        sys.exit(1)

    algorithm_number = sys.argv[2] if len(sys.argv) > 2 else None
    if algorithm_number not in algorithm_mapping:
        print("Niepoprawny numer algorytmu!")
        sys.exit(1)

    # Wczytaj dane wejściowe z STDIN
    input_data = sys.stdin.read().strip().split()
    input_data = list(map(int, input_data))

    # Uruchom wybrany algorytm
    sorted_data = algorithm_mapping[algorithm_number](input_data)

    # Wypisz wynik
    print(" ".join(map(str, sorted_data)))
