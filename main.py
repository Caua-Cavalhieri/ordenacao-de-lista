#O corte antecipado da versão otimizada economiza mais passagens em listas já ordenadas ou quase ordenadas. 
# Isso acontece porque, a cada passagem, o algoritmo verifica se houve alguma troca: 
# se não houve, significa que a lista já está ordenada, e o laço é interrompido antes do tempo.
#Em uma lista já ordenada, nenhuma troca ocorre logo na primeira passagem, então o algoritmo para imediatamente 
# (1 passagem, em vez de n-1). Em uma lista quase ordenada, poucas trocas são necessárias, 
# e o algoritmo também para bem antes do limite máximo.
#Já no pior caso, uma lista em ordem totalmente inversa, 
# praticamente todas as passagens resultam em pelo menos uma troca, 
# então o corte antecipado só ocorre na última passagem possível — não havendo economia real nesse cenário.



from bubble_sort import bubble_sort, bubble_sort_otimizado
from utilitarios import ler_lista_do_usuario, exibir_resultado
#---------------------------------------------------------------#

def exibir_menu():
   print("")
   print("1. Bubble Sort (versão básica)")
   print("2. Bubble Sort (versão otimizada)")
   print("0. Sair")

#---------------------------------------------------------------#

def main():
   opcao = -1
   while opcao != 0:
      exibir_menu()
      entrada = input("Escolha uma opção: ")
      try:
         opcao = int(entrada)
      except ValueError:
         print("Opcao invalida.")
      if opcao == 1:
         lista = ler_lista_do_usuario()
         resultado = bubble_sort(list(lista))
         exibir_resultado("Bubble Sort básico", resultado)
      elif opcao == 2:
         lista = ler_lista_do_usuario()
         resultado = bubble_sort_otimizado(list(lista))
         exibir_resultado("Bubble Sort otimizado", resultado)
      elif opcao == 0:
         print("Encerrando o programa.")
      else:
         print("Opcao invalida. Tente novamente.")


#---------------------------------------------------------------#
if __name__ == "__main__":
   main()