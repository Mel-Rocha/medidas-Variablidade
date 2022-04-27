'''
Objetivo:
<lerTxt>       Ler uma arquivo TXT com dados numéricos 
               Calcular e apresentar as seguintes medidas:
<max>          Máximo
<min>          Mínimo
<amp>          Amplitude
<media>        Média
<mediana>      Mediana
<variancia>    Variância 
<dvp> Desvio   Padrão
Não utilizem   bibliotecas
'''

#<lerTxt>

file = open('arquivo.txt', 'r') 
dados_aux = file.readlines()
file.seek(0)
file.close

dados = []

for i in dados_aux:
  dados.append(float(i.rstrip()))
  


dados.sort()

'''
Abertura do arquivo txt por meio do método open utlizando o parametro 'r', que indica que o arquivo será aberto apenas para leitura. A função readlines() transforma a variável (file) em uma lista, file seek com o parametro 0 retorna o ponteiro de leitura para o início do arquivo, file close fecha o arquivo.

O laço de repetição for sobre a lista (dados_aux) é utilizado para a função (rstrip()) percorrer a lista e ser executada removendo os caracteres especias.

O método sort() é utlizado para ordenar de forma crescente os dados.
'''

#</lerTxt>


print('Os dados inseridos são para população ou amostra: ')
p_a = input('[]p  []a  ')

#<min> 

print('')
min = float(dados[0])
print(f'Mínimo: {min}')
'''
A lista dados está ordenada de forma crescente, portanto o indice 0 é o valor mínimo. 
'''

#</min> 

#<max> 
max = float(dados[-1])
print(f'Máximo: {max}')
'''
O indice -1 é o último valor da lista, portanto ele é o elemento máximo.
'''

#</max> 

#<amp>
amp = max - min

print(f'Amplitude: {amp:.2f}')
'''
A amplitude é a diferença entre o max e o min
'''

#</amp>

#<mediana>  
len_dados = len(dados)
imp_par = len(dados) % 2



if imp_par == 0:
  mediana = (dados[int(len_dados / 2)] + dados[int((len_dados / 2) - 1)]) / 2
  print(f'Mediana: {mediana}')
if imp_par == 1:
  mediana = dados[int((len_dados / 2))]
  print(f'Mediana: {mediana}')
'''
Se os dados possuirem uma quantidade par a mediana será feita de uma forma, senão outro cálculo será empregado
'''

#</mediana> 

#<media> 
soma = 0
for i in dados:
  soma += i

media = soma / len_dados
print(f'Média: {media}')
'''
o laço for é feito para percorrer a lista (dados) e a variavel (soma) ganha o incremento de (i).
'''
#<media>

#<variancia>
dvp = []
dvp_quad = []
for i in dados:
  dvm = i - media
  dvp.append(dvm)

  
#print(dvp)

for i in dvp:
  x = i ** 2
  dvp_quad.append(x)



soma_dvp_quad = 0
for i in dvp_quad:
  soma_dvp_quad += i

len_dvp_quad = len(dvp_quad)
variancia_p = soma_dvp_quad / len_dvp_quad
variancia_a = soma_dvp_quad / (len_dvp_quad - 1)




#</variancia> 

#<dvp> 
dvp_p = variancia_p ** 0.5
dvp_a = variancia_a ** 0.5
#</dvp> 

if p_a == 'p':
  print(f'Variância Populacional: {variancia_p:.2f}')
  print(f'Desvio Padrão Populacional: {dvp_p:.2f}')
if p_a == 'a':
  print(f'Variância Amostral: {variancia_a:.2f}')
  print(f'Desvio Padrão Amostral: {dvp_a:.2f}')
  