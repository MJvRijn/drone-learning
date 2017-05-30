from pynput import keyboard

class KeyboardListener(object):
    _up_active = False
    _left_active = False
    _right_active = False
    _pgup_active = False
    _pgdown_active = False

    def __init__(self):
        print('HOVER')

        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


    def on_press(self, key):
        if key == keyboard.Key.up and not self._up_active:
            print('FORWARD')
            self._up_active = True

        elif key == keyboard.Key.left and not self._left_active:
            print('ANTICLOCKWISE')
            self._left_active = True

        elif key == keyboard.Key.right and not self._right_active:
            print('CLOCKWISE')
            self._right_active = True

        elif key == keyboard.Key.page_up and not self._pgup_active:
            print('START')
            self._pgup_active = True

        elif key == keyboard.Key.page_down and not self._pgdown_active:
            print('STOP')
            self._pgdown_active = True

    def on_release(self, key):
        if key == keyboard.Key.up:
            self._up_active = False
        elif key == keyboard.Key.left:
            self._left_active = False
        elif key == keyboard.Key.right:
            self._right_active = False
        elif key == keyboard.Key.page_up:
            self._pgup_active = False
        elif key == keyboard.Key.page_down:
            self._pgdown_active = False
        else:
            return

        if not (self._up_active or self._left_active or self._right_active or self._pgup_active or self._pgdown_active):
            print('HOVER')

KeyboardListener()
