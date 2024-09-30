
# def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
#     pass
#     target_number = None
#     return target_number

# from tools import *
# from data import *
# assert bin_dec_hex__to__bin_dec_hex ("101", 2, 10) == "5"

# def do_the_job ():
#     init_number = ask_for_the_init_number ()
#     init_base = ask_for_the_init_base ()
#     target_base = ask_for_the_target_base ()
#     target_number = \
#       bin_dec_hex__to__bin_dec_hex (init_number, \
#                                     init_base, \
#                                     target_base)

# do_the_job ()




def bin_dec_hex__to__bin_dec_hex(init_number, init_base, target_base):
    # Conversion en décimal
    if init_base == 2:  # Binaire à Décimal
        decimal_number = 0
        for i, digit in enumerate(reversed(init_number)):
            decimal_number += int(digit) * (2 ** i)
    elif init_base == 10:  # Décimal à Décimal
        decimal_number = int(init_number)  # On peut directement utiliser int
    elif init_base == 16:  # Hexadécimal à Décimal
        decimal_number = 0
        hex_digits = "0123456789abcdef"
        for i, digit in enumerate(reversed(init_number.lower())):
            decimal_number += hex_digits.index(digit) * (16 ** i)
    else:
        return None  # Base invalide

    # Conversion vers la base cible
    if target_base == 2:  # Décimal à Binaire
        if decimal_number == 0:
            return "0"
        binary_number = ""
        while decimal_number > 0:
            binary_number = str(decimal_number % 2) + binary_number
            decimal_number //= 2
        return binary_number
    elif target_base == 10:  # Décimal à Décimal
        return str(decimal_number)
    elif target_base == 16:  # Décimal à Hexadécimal
        if decimal_number == 0:
            return "0"
        hex_number = ""
        hex_digits = "0123456789abcdef"
        while decimal_number > 0:
            hex_number = hex_digits[decimal_number % 16] + hex_number
            decimal_number //= 16
        return hex_number
    else:
        return None  # Base cible invalide


def ask_for_the_init_number():
    return input("Entrez le nombre à convertir: ")


def ask_for_the_init_base():
    print("Choisissez la base d'origine:")
    print("1: Binaire (2)")
    print("2: Décimal (10)")
    print("3: Hexadécimal (16)")
    choice = int(input("Entrez votre choix (1/2/3): "))
    return {1: 2, 2: 10, 3: 16}.get(choice, None)


def ask_for_the_target_base():
    print("Choisissez la base cible:")
    print("1: Binaire (2)")
    print("2: Décimal (10)")
    print("3: Hexadécimal (16)")
    choice = int(input("Entrez votre choix (1/2/3): "))
    return {1: 2, 2: 10, 3: 16}.get(choice, None)


def do_the_job():
    init_number = ask_for_the_init_number()
    init_base = ask_for_the_init_base()
    target_base = ask_for_the_target_base()
    
    if init_base is None or target_base is None:
        print("Choix de base invalide.")
        return
    
    target_number = bin_dec_hex__to__bin_dec_hex(init_number, init_base, target_base)
    
    if target_number is not None:
        print(f"Le nombre {init_number} en base {init_base} est {target_number} en base {target_base}.")
    else:
        print("Erreur dans la conversion.")


if __name__ == "__main__":
    do_the_job()

