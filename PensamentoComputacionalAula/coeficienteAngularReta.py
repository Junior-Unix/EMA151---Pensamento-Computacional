 # 4. Construa um programa que determine qual ´ e o coeficiente angular da reta que
 # passa por dois pontos que devem ser digitados pelo usu´ ario. A mensagem na tela
 # deve ser a seguinte:
 # O coeficiente angular da reta que passa pelos pontos (x,y) e (x,y) ´ e igual a xxx.
 # ESSE PROGRAMA EXIGE O MATPLOTLIB, BIBLIOTECA QUE TEM QUE SER INSTALADA
# # ANTES DE RODAR O PROGRAMA.

#
while True:
    # Solicitar os valores dos dois pontos
    x1 = input("Digite o valor de x1 (ou '(q)uit' para encerrar): ")
    if x1.lower() == 'q':
        break
    y1 = input("Digite o valor de y1: ")
    x2 = input("Digite o valor de x2: ")
    y2 = input("Digite o valor de y2: ")

    # Converter os valores para float
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    # Verificar se x1 é igual a x2 para evitar divisão por zero
    if x1 == x2:
        print("Os pontos ({}, {}) e ({}, {}) formam uma reta vertical, e o coeficiente angular é indefinido.".format(x1, y1, x2, y2))
    else:
        # Calcular o coeficiente angular
        coeficiente_angular = (y2 - y1) / (x2 - x1)

        # Exibir o resultado
        print("O coeficiente angular da reta que passa pelos pontos ({}, {}) e ({}, {}) é igual a {:.2f}".format(x1, y1, x2, y2, coeficiente_angular))
    # Plote a reta
    import matplotlib.pyplot as plt

    # Definir os pontos da reta
    x_values = [x1, x2]
    y_values = [y1, y2]

    # Criar o gráfico
    plt.plot(x_values, y_values, marker='o')

    # Adicionar título e rótulos aos eixos
    plt.title('Reta que passa pelos pontos ({}, {}) e ({}, {})'.format(x1, y1, x2, y2))
    plt.xlabel('x')
    plt.ylabel('y')

    # Exibir o gráfico
    plt.grid(True)
    plt.show()