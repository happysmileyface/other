from pynput import keyboard

def on_press(key):
    try:
        return '{0}'.format(
            key.charaaaa)
    except AttributeError:
        return '{0}'.format(
            key)

def on_release(key):
    print('{0}'.format(
        key.char))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
if __name__ == "__main__":
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

# ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()