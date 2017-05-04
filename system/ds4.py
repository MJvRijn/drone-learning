import struct, time, os

class ds4():
    BUTTON_TAKEOFF = 'L1'
    BUTTON_LAND = 'R1'
    BUTTON_UP = 'cross'
    BUTTON_DOWN = 'circle'

    axis_map = {0: 'left_horizontal', 1: 'left_vertical', 2: 'L2_axis', 3: 'right_horizontal',
                4: 'right_vertical', 5: 'R2_axis', 6: 'leftright', 7: 'updown'}
    button_map = {0: 'cross', 1: 'circle', 2: 'triangle', 3: 'square', 4: 'L1',
                  5: 'R1', 6: 'L2_button', 7: 'R2_button', 8: 'share', 9: 'options',
                  10: 'PS', 11: 'L3', 12: 'R3'}

    persistent_buttons = []
    persistent_axes = []

    debug = False

    def __init__(self):
        self.device = os.open('/dev/input/js0', os.O_NONBLOCK)
        self.airborne = False

    def process_inputs(self):
        buttons = []
        axes = []

        while True:
            try:
                event_buffer = os.read(self.device, 8)
            except BlockingIOError:
                break

            time, value, event_type, number = struct.unpack('IhBB', event_buffer)

            if event_type == 1: # Button
                if self.button_map[number] == self.BUTTON_TAKEOFF and value == 1:
                    if self.debug: print('TAKEOFF')
                    buttons.append('TAKEOFF')

                elif self.button_map[number] == self.BUTTON_LAND and value == 1:
                    if self.debug: print('LAND')
                    buttons.append('LAND')

                elif self.button_map[number] == self.BUTTON_UP:
                    if value == 1:
                        if self.debug: print('UP')
                        self.persistent_buttons.append('UP')
                    elif value == 0:
                        self.persistent_buttons.remove('UP')


                elif self.button_map[number] == self.BUTTON_DOWN:
                    if value == 1:
                        if self.debug: print('DOWN')
                        self.persistent_buttons.append('DOWN')
                    elif value == 0:
                        self.persistent_buttons.remove('DOWN')

                if self.debug:
                    print("Button")
                    print(value)
                    print(number)
                    print("")

            elif event_type == 2: # Axis
                print("Axis")
                print(value)
                print(number)

        return (self.persistent_buttons + buttons), (self.persistent_axes + axes)



    def get_action(self):
        buttons, axes = self.process_inputs()

        if not self.airborne and 'TAKEOFF' not in buttons:
            return 'HOVER'

        elif len(buttons) == 0 and len(axes) == 0:
            return 'HOVER'

        elif 'TAKEOFF' in buttons:
            self.airborne = True;
            return 'TAKEOFF'

        elif 'LAND' in buttons:
            self.airborne = False
            return 'LAND'

        elif 'UP' in buttons:
            return 'UP'
        elif 'DOWN' in buttons:
            return 'DOWN'






        # if type & 0x80:
        #      print("(initial)")
        #
        # if type & 0x01:
        #     button = button_map[number]
        #     if button:
        #         button_states[button] = value
        #         if value:
        #             print "%s pressed" % (button)
        #         else:
        #             print "%s released" % (button)
        #
        # if type & 0x02:
        #     axis = axis_map[number]
        #     if axis:
        #         fvalue = value / 32767.0
        #         axis_states[axis] = fvalue
        #         print "%s: %.3f" % (axis, fvalue)

controller = ds4()
while True:
    action = controller.get_action()
    print(action)
    time.sleep(1/10)
