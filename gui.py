# Função para ler o número inserido pelo utilizador
def read_number(question):
    while True:
        num = input(question)
        if num.isnumeric():
            break
        else:
            print("Introduza um número")
    return int(num)


# Função para criar o menu de escolhas do utilizador
def menu():
    print("""
###############################
#         Calculadora         #
#                             #
#                             #
# 1 - Soma                    #
# 2 - Subtração               #
# 3 - Multiplicação           #
# 4 - Divisão                 #
# 5 - Potencia                #
# 6 - Raiz Quadrada           #
# 7 - Percentagem             #
# 8 - Sair                    #
###############################
""")


# Função para selecionar uma operação do menu
def escolha_menu(dictEscolhas):
    while True:
        choice = read_number("Escolha uma opção: ")
        if choice >= 1 and choice <= 7:
            numA = read_number("Digite o primeiro número: ")
            numB = read_number("Digite o segundo número: ")
            print(dictEscolhas[choice](numA, numB))
        elif choice == 8:
            break
