import pandas as pd
vendas_bd = pd.read_excel('Vendas.xlsx')
vendas_slice = vendas_bd['Valor Unitário']
sales = vendas_slice[:15000]
def bucket_sort(arr):
    # Obter o valor máximo e mínimo do array
    max_value = max(arr)
    min_value = min(arr)
    
    # Calcular o tamanho dos baldes e o número total de baldes
    bucket_size = (max_value - min_value) // len(arr) + 1
    bucket_count = (max_value - min_value) // bucket_size + 1
    
    # Inicializar os baldes
    buckets = [[] for _ in range(bucket_count)]
    
    # Adicionar cada elemento ao balde apropriado
    for num in arr:
        bucket_index = (num - min_value) // bucket_size
        buckets[bucket_index].append(num)
    
    # Ordenar cada balde individualmente usando o algoritmo de inserção
    for i in range(bucket_count):
        insertion_sort(buckets[i])
    
    # Juntar os baldes ordenados em um único array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += bucket
    
    print(sorted_arr)

# Função auxiliar para ordenar cada balde individualmente usando o algoritmo de inserção
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key_item

bucket_sort(sales)
print(len(sales))
