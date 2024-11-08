
from data import*

# Convertit un nombre binaire en décimal
def bin_to_dec(bin_number):
    return int(bin_number, 2)

# Convertit un nombre décimal en binaire
def dec_to_bin(dec_number):
    if dec_number == 0:
        return "0"
    binary_number = ""
    while dec_number > 0:
        binary_number = str(dec_number % 2) + binary_number
        dec_number //= 2
    return binary_number

# Convertit un nombre hexadécimal en décimal
def hex_to_dec(hex_number):
    return int(hex_number, 16)
 

# Convertit un nombre décimal en hexadécimal
def dec_to_hex(dec_number):
    if dec_number == 0:
        return "0"
    hex_number = ""
    while dec_number > 0:
        hex_number = hex_valid_char[dec_number % 16] + hex_number
        dec_number //= 16
    return hex_number
 
 # Convertit un nombre binaire en hexadécimal
def bin_to_hex(bin_number):
    decimal_number = bin_to_dec(bin_number)
    return dec_to_hex(decimal_number)


# Convertit un nombre hexadécimal en binaire
def hex_to_bin(hex_number):
    decimal_number = hex_to_dec(hex_number)
    return dec_to_bin(decimal_number)


# Convertit un nombre entre les bases binaire, décimale et hexadécimale
def bin_dec_hex_to_bin_dec_hex(init_number, init_base, target_base):
    if init_base == 2:
        decimal_number = bin_to_dec(init_number)
    elif init_base == 10:
        decimal_number = int(init_number)
    elif init_base == 16:
        decimal_number = hex_to_dec(init_number)
    else:
        return None  # Base invalide

    if target_base == 2:
        return dec_to_bin(decimal_number)
    elif target_base == 10:
        return str(decimal_number)
    elif target_base == 16:
        return dec_to_hex(decimal_number)
    else:
        return None  # Base cible invalide

def check_valid_char(char):
    return char in hex_valid_char

def check_char_number_validity(char):
    return check_valid_char(char)


def is_not_valid_number(init_number):
    for char in init_number:
        valid_number= char in valid_chars
        if valid_number == False:
            return True
        return False

