# Projeto_ED_Sort
Leandro Alencar Lira 					Matrícula: 22112409-Tim sort
Mauro Santos da Paz   				Matrícula: 22110822-Bucket sort
Samuel Jonas Cavalcante Lima			Matrícula: 22112463-Radix sort

Tim sort: O Tim Sort é um algoritmo de ordenação híbrido, que combina as técnicas de Merge Sort e Insertion Sort. Ele divide a lista em blocos menores
e aplica o Insertion Sort a cada bloco para obter blocos ordenados. Em seguida, esses blocos ordenados são combinados usando a operação de merge do
Merge Sort. O Tim Sort é eficiente para listas de qualquer tamanho e apresenta um bom desempenho para listas parcialmente ordenadas. Além disso, ele
possui uma complexidade assintótica de O(n log n) no pior caso, tornando-o uma opção muito eficiente para a maioria das situações de ordenação. 


Bucket sort: O Bucket Sort é um algoritmo de ordenação que divide um conjunto de elementos em “baldes” ou compartimentos, classificando cada balde
individualmente usando um algoritmo de ordenação. Ele é útil quando os elementos a serem ordenados estão uniformemente distribuídos em um intervalo 
ou podem ser divididos em baldes gerenciáveis. A complexidade total do Bucket Sort no pior caso é O(n^2), uma vez que o pior caso ocorre quando todos
os elementos estão no mesmo balde e o Insertion Sort precisa ser executado em todos os elementos. No entanto, em casos médios ou em listas parcialmente
ordenadas, o Bucket Sort pode ter um desempenho muito melhor, com uma complexidade média de O(n+k), onde k é o número de baldes. 


Radix sort: O Radix Sort é um algoritmo de ordenação que ordena uma lista ou array baseado nos dígitos de seus elementos. Ele agrupa os elementos
de acordo com cada um de seus dígitos, começando pelo dígito menos significativo e, em seguida, ordenando os elementos em cada grupo. O processo
é repetido para cada dígito, do menos significativo ao mais significativo, até que todos os elementos estejam ordenados. O Radix Sort é eficiente
em certas situações, especialmente quando o número de elementos a serem ordenados é grande e o número de dígitos é relativamente pequeno. A 
complexidade do algoritmo Radix Sort é de O(kn), onde k é o número máximo de dígitos dos elementos da lista e n é o tamanho da lista.


Projetos rodados em um computador com as seguintes configurações de hardware:
i5 11ª geração
8gb de memória ram

Conclusão: Neste texto, apresentamos três algoritmos de ordenação e suas características: Tim Sort, Bucket Sort e Radix Sort. Cada algoritmo
possui suas vantagens e desvantagens, e a escolha do algoritmo adequado depende das características dos dados a serem ordenados. Além disso, 
tivemos o resultado da seguinte maneira: radix sort e bucket empatados em primeiro com 5.5 segundos para ordenar uma lista de 15k de items, 
já o tim sort ficou um pouco atrás com 5.8 segundos

Obs.: Tivemos um pequeno problema com o repositório enviado anteriormente ao senhor, disponibilizamos o código e o banco de dados no seguinte
respositório: https://github.com/SamuelEternal/Projeto_ED_Sort
