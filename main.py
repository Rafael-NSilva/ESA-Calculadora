from logic import *
from gui import *


def main():
    dic = {1: sum,
           2: subtraction,
           3: multiply,
           4: div,
           5: pow,
           6: square_root,
           7: percentage}
    menu()
    escolha_menu(dic)


if __name__ == "__main__":
    main()
