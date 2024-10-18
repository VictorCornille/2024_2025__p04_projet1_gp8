from data import*
from tools import*
  # Base cible invalide

def bin_dec_hex_to_bin_dec_hex(init_number, init_base, target_base):
    # Conversion en décimal
    if init_base == 2:  # Binaire à Décimal
        decimal_number = 0
        for i, number in enumerate(reversed(init_number)):
            decimal_number += int(number) * (2 ** i)
    elif init_base == 10:  # Décimal à Décimal
        decimal_number = int(init_number)  # On peut directement utiliser int
    elif init_base == 16:  # Hexadécimal à Décimal
        decimal_number = 0
        for i, number in enumerate(reversed(init_number.lower())):
            decimal_number += hex_number.index(number) * (16 ** i)
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
    elif target_base == 16:  # Décimal à Hexadécimal    
            return "0"
    hex_number = ""
    while decimal_number > 0:
            hex_number = hex_valid_char[decimal_number % 16] + hex_number
            decimal_number //= 16
            return hex_number
    else:
         return None  # Base cible invalide


if __name__== "__main__":
    do_the_job()