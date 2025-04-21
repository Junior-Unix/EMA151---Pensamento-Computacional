print("\033[31;40mOs pilares do Pensamento Computacional são:\033[0m")
print("\033[31;40mDecomposição:\033[32;40m Dividir um problema ou sistema complexo em partes menores e mais gerenciáveis.\033[0m")
print("\033[31;40mReconhecimento de padrões:\033[32;40m Identificar semelhanças ou tendências dentro dos dados ou problemas.\033[0m")
print("\033[31;40mAbstração:\033[32;40m Focar nos aspectos essenciais de um problema, descartando detalhes irrelevantes.\033[0m")
print("\033[31;40mAlgoritmos:\033[32;40m Desenvolver sequências de passos ou instruções para resolver problemas ou completar tarefas.\033[0m")
def mostrar_abstracao():
    print("Exemplo de Abstração:")
    print("""
def calcular_area_retangulo(largura, altura):
    return largura * altura

print(calcular_area_retangulo(5, 3))
    """)

def mostrar_decomposicao():
    print("Exemplo de Decomposição:")
    print("""
def preparar_ingredientes():
    print("Preparando ingredientes...")

def cozinhar():
    print("Cozinhando...")

def servir():
    print("Servindo...")

preparar_ingredientes()
cozinhar()
servir()
    """)

def mostrar_padroes():
    print("Exemplo de Reconhecimento de Padrões:")
    print("""
for i in range(5):
    print("Padrão", i)
    """)

def mostrar_algoritmos():
    print("Exemplo de Algoritmos:")
    print("""
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(5))
    """)

def menu():
    while True:
        print("\n\033[32mMenu:\033[0m")
        print("\033[31m1.\033[0m \033[32mAbstração\033[0m")
        print("\033[31m2.\033[0m \033[32mDecomposição\033[0m")
        print("\033[31m3.\033[0m \033[32mReconhecimento de Padrões\033[0m")
        print("\033[31m4.\033[0m \033[32mAlgoritmos\033[0m")
        print("\033[31m5.\033[0m \033[32mSair\033[0m")
        escolha = input("Selecione uma opção: ")

        if escolha == '1':
            mostrar_abstracao()
        elif escolha == '2':
            mostrar_decomposicao()
        elif escolha == '3':
            mostrar_padroes()
        elif escolha == '4':
            mostrar_algoritmos()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()