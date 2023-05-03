import pandas as pd
vendas_bd = pd.read_excel('Vendas.xlsx')
valor_unitário = vendas_bd['Valor Unitário']
sales = valor_unitário[:15000]


def radix_sort(lista):
    # Determinando o número máximo de dígitos
    max_dig = len(str(max(lista)))
    
    # Loop pelos dígitos, do menos significativo para o mais significativo
    for d in range(max_dig):
        # Criando as listas de baldes
        balde = [[] for _ in range(10)]
        
        # Colocando cada número no balde correspondente
        for num in lista:
            dig = (num // 10**d) % 10
            balde[dig].append(num)
        
        # Juntando os baldes na lista original
        lista = []
        for b in balde:
            lista.extend(b)
    
    return lista

# Exemplo de uso
lista = valor_unitário
print("Lista original:", lista[:1500])
print("Lista ordenada:", radix_sort(sales))
print(len(sales))

