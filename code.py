from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, Key
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.lock_status import LockStatus
from kmk.extensions.LED import LED
from kmk.modules.layers import Layers
import board
import digitalio
#import os, sys
#print(os.uname())
#print(sys.version)

keyboard = KMKKeyboard()

#pins
keyboard.row_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4]
keyboard.col_pins = [board.GP10, board.GP11, board.GP12, board.GP13,
                     board.GP14, board.GP15, board.GP26, board.GP27]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#split config
split = Split(
    split_target_left=True,
    split_flip=False,
    split_side=SplitSide.LEFT,
    data_pin=board.GP8,
    split_type=SplitType.UART,
    uart_interval=20,
    use_pio=True

)
keyboard.modules.append(split)
keyboard.modules.append(MediaKeys())

locks = LockStatus()
keyboard.extensions.append(locks)

#led setup
capsled = digitalio.DigitalInOut(board.GP7)
capsled.direction = digitalio.Direction.OUTPUT
capsled.value = False


gled = digitalio.DigitalInOut(board.GP6)
gled.direction = digitalio.Direction.OUTPUT
gled.value = False


#layer setup
layers = Layers()
keyboard.modules.append(layers)
#capslock led
#class LEDLockStatus(LockStatus):

 #   def set_lock_leds(self):
 #       if self.get_caps_lock():
 #           capsled.value = True
  #      else: 
  #          capsled.value = False

   # def after_hid_send(self, sandbox):
    #    super().after_hid_send(sandbox)
    #    if self.report_updated:
    #        self.set_lock_leds()


#keyboard.extensions.append(LEDLockStatus())


#custom keys
MOMENTARY = KC.MO(1)
layer_2 = False
          

def toggle_game_layer(*args):

    global layer_2
    layer_2 = not layer_2
    if layer_2:
        keyboard.active_layers = [2]
        gled.value = True
    else:
        keyboard.active_layers = [0]
        gled.value = False

    return False

LAYER_2_TOGGLE = Key(on_press=toggle_game_layer)
#keymap


keyboard.keymap = [
    [KC.LSFT(KC.LGUI(KC.S)), KC.ESC,  KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.NO, 	KC.NO, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSLASH, KC.MEDIA_PLAY_PAUSE,
    KC.MEDIA_NEXT_TRACK, KC.LSHIFT, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.TAB, 			LAYER_2_TOGGLE, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET,
    KC.NO, KC.NO, KC.A, KC.S, KC.D, KC.F, KC.G, KC.NO, 					KC.NO, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.NO, KC.NO,
    KC.NO, KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.NO, 					KC.NO, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.NO, KC.NO,
    KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LCTL, KC.SPACE, KC.LGUI, 			MOMENTARY, KC.ENTER, KC.LSHIFT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO],

    [KC.LSFT(KC.LGUI(KC.S)), KC.ESC,  KC.N1, KC.N2, KC.F3, KC.N4, KC.N5, KC.LCTL(KC.LALT), 	KC.CAPS, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSLASH, KC.MEDIA_PLAY_PAUSE,
    KC.MEDIA_PREV_TRACK, KC.TAB, KC.TILDE, KC.W, KC.UP, KC.R, KC.T, KC.NO, 			LAYER_2_TOGGLE, KC.MINUS, KC.EQUAL, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET,
    KC.NO, KC.NO, KC.A, KC.LEFT, KC.DOWN, KC.RIGHT, KC.G, KC.NO, 					KC.NO, KC.UNDS, KC.PLUS, KC.K, KC.L, KC.QUOTE, KC.NO, KC.NO,
    KC.NO, KC.NO, KC.HOME, KC.X, KC.LCTL(KC.LSFT(KC.C)), KC.LCTL(KC.LSFT(KC.V)), KC.B, KC.DEL, 					KC.LCTL(KC.LALT(KC.KP_0)), KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.NO, KC.NO,
    KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LALT, KC.TAB, KC.BSPACE, 			MOMENTARY, KC.ENTER, KC.LSHIFT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO],

    [KC.LSFT(KC.LGUI(KC.S)), KC.ESC,  KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.NO, 	KC.NO, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSLASH, KC.MEDIA_PLAY_PAUSE,
    KC.MEDIA_PREV_TRACK, KC.TAB, KC.GRAVE, KC.Q, KC.W, KC.E, KC.R, KC.NO, 			LAYER_2_TOGGLE, KC.MINUS, KC.EQUAL, KC.I, KC.O, KC.P, KC.F1, KC.F2,
    KC.NO, KC.NO, KC.LSHIFT, KC.A, KC.S, KC.D, KC.F, KC.G, 					KC.NO, KC.UNDS, KC.PLUS, KC.K, KC.L, KC.QUOTE, KC.NO, KC.NO,
    KC.NO, KC.NO, KC.LCTL, KC.Z, KC.X, KC.C, KC.B, KC.NO, 					KC.NO, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.NO, KC.NO,
    KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.SPACE, KC.SPACE, KC.SPACE, 			MOMENTARY, KC.ENTER, KC.CAPS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO],





]
if __name__ == "__main__":
    keyboard.go()


