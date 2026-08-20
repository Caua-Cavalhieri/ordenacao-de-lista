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