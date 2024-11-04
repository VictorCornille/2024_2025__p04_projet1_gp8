from tools import*
from data import*
       
         
def ask_for_the_init_number():
    init_number = input("Entrez le nombre à convertir: ")
    while is_not_valid_number(init_number):
        init_number = input("Entrez un autre nombre à convertir: ")
    return init_number


def ask_for_the_init_base():
    print("Choisissez la base d'origine:")
    print("   1: Binaire (2)")
    print("   2: Décimal (10)")
    print("   3: Hexadécimal (16)")
    choice = int(input("Entrez votre choix (1/2/3): "))
    return{1:2, 2:10, 3:16}.get(choice, None)


def ask_for_the_target_base():
    print("Choisissez la base cible:")
    print("   1: Binaire (2)")
    print("   2: Décimal (10)")
    print("   3: Hexadécimal (16)")
    choice = int(input("Entrez votre choix (1/2/3): "))
    return {1:2, 2:10, 3:16}.get(choice, None)


def do_the_job():
    init_number = ask_for_the_init_number()
    init_base = ask_for_the_init_base()
    target_base = ask_for_the_target_base()
    if init_base is None or target_base is None:
            print("Choix de base invalide.")
    target_number = bin_dec_hex_to_bin_dec_hex (init_number, init_base, target_base)
    if target_number is not None:
            print(f"Le nombre {init_number} en base {init_base} est {target_number} en base {target_base}.")
    else:
            print("Erreur dans la conversion.")
            


do_the_job ()