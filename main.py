from tools import *
from data import*


def bin_dec_hex__to__bin_dec_hex (init_number,\
                                   init_base,\
                                      target_base):
    target_number = None
    return target_number




def do_the_job ():
    init_number = ask_for_the_init_number()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
      bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)

def do_the_job():
    init_number = ask_for_the_init_number()
    init_base = ask_for_the_init_base()
    target_base = ask_for_the_target_base()
    
    if init_base is None or target_base is None:
        print("Choix de base invalide.")
        return
    
    target_number = bin_dec_hex_to_bin_dec_hex (init_number, init_base, target_base)
    
    if target_number is not None:
        print(f"Le nombre {init_number} en base {init_base} est {target_number} en base {target_base}.")
    else:
        print("Erreur dans la conversion.")