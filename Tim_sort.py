import pandas as pd
vendas_bd = pd.read_excel('Vendas.xlsx')
valor_unitário = vendas_bd['Valor Unitário']
sales = valor_unitário[:15000]
v=[]
for i in sales:
    v.append(i)


def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

    return arr


def merge(arr_A, arr_B):
    arr_C = []
    i, j = 0, 0
    while i < len(arr_A) and j < len(arr_B):
        if arr_A[i] < arr_B[j]:
            arr_C.append(arr_A[i])
            i += 1
        else:
            arr_C.append(arr_B[j])
            j += 1
    if i == len(arr_A):
        arr_C.extend(arr_B[j:])
    else:
        arr_C.extend(arr_A[i:])
    return arr_C


def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(
                arr[start:midpoint + 1], arr[midpoint + 1:end + 1])
            arr[start:start + len(merged_array)] = merged_array

        size *= 2

    return arr

print(timsort(v))
