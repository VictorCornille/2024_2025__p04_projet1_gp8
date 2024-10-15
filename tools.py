
from data import*
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
def check_valid_char(char):
       return char in hex_valid_char
       
 
def check_char_number_validity (char):
    return char in hex_valid_char

                      
def is_a_valid_number (number):
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i <= len (number) - 1:
        is_a_valid_char = check_char_number_validity (number [i])
        i = i + 1
    return is_a_valid_char                     



def ask_for_the_init_number ():
    init_number = input (ask_for_init_number_text)
    while not (is_a_valid_number (init_number)) == True:
        init_number = input (ask_again_for_init_number_text)
    return init_number


def decimal_o_hexadecimal_to_bin (n,d):
     restes=""
     q= n // d
     while q > 0 :
          reste = n % d
          restes = reste + restes
          n = q
          q = n // 2
          return restes


def ask_for_the_init_base ():
     pass
#    si binaire alors =2
#    si decimal alors =10
#    si hexadecimal alors =16
    
       

def ask_for_the_target_base():
     pass

def bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base):
     pass
#  Fonction 1 qui passe de binaire a decimal
#  Fonction 2 qui passe de binaire a hexa
#  Fonction 3 qui passe de decimal a binaire (l'inverse de la fonction 1)
#  Fonction 4 qui passe de decimal a hexa
#  Fonction 5 qui passe de hexa a binaire (l'inverse de la fonction 2)
#  Fonction 6 qui passe de hexa a decimal (l'inverse de la fonction 4)
