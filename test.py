def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Początkowy przyrost
    
    while gap > 0:
        print(f'Przyrost: {gap}')
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
            print(f'Po wstawieniu {key}: {arr}')
        gap //= 2  # Zmniejszamy przyrost o połowę
    
    return arr

# Przykładowe użycie
arr = [4, 14, 7, 2, 1, 10, 3, 8, 11, 5, 12]
sorted_arr = shell_sort(arr)
print("Posortowana tablica:", sorted_arr)