def ler_lista_do_usuario():
   while True:
      entrada = input("Digite os números separados por espaço: ")
      partes = entrada.split()
      try:
         lista = [int(valor) for valor in partes]
         return lista
      except ValueError:
         print("Entrada inválida. Use apenas inteiros.")

#--------------------------------------------------------------------#

def exibir_resultado(nome_algoritmo, lista_ordenada):
   print("Algoritmo utilizado: " + nome_algoritmo)
   print("Lista ordenada: " + str(lista_ordenada))