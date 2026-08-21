# O Bubble Sort otimizado usa o histórico de trocas para decidir quando parar mais cedo, 
# o Selection Sort sempre faz a varredura completa para achar o mínimo, 
# então seu número de comparações é fixo e não depende de a lista já estar ordenada.
#-------------------------------------------------------------------------------------------#

def selection_sort(lista):
   n = len(lista)
   comparacoes = 0
   trocas = 0
   for i in range(n - 1):
      indice_menor = i
      for j in range(i + 1,n):
         comparacoes += 1
         if lista[j] < lista[indice_menor]:
            indice_menor= j
      if indice_menor !=i:
         lista[i], lista[indice_menor] = \
            lista[indice_menor], lista[i]
         trocas += 1
   print ("comparacoes=" + str(comparacoes))
   print ("trocas=" + str(trocas))
   return lista

# selection_sort([1, 2, 3, 4, 5])
# comparacoes=10
# trocas=0