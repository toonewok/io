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
#print('hi mom')

keyboard = KMKKeyboard()

#pins
keyboard.row_pins = [board.GP4, board.GP5, board.GP6, board.GP7, board.GP25]
keyboard.col_pins = [board.GP10, board.GP0, board.GP1, board.GP2, board.GP3]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#split config
split = Split(
    split_target_left=True,
    split_flip=True,
    split_side=SplitSide.LEFT,
    data_pin=board.GP8,
    data_pin2=board.GP9,
    split_type=SplitType.UART,
    uart_interval=20,
    use_pio=True

)
keyboard.modules.append(split)
keyboard.modules.append(MediaKeys())

locks = LockStatus()
keyboard.extensions.append(locks)

#led setup


gled = digitalio.DigitalInOut(board.GP11)
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
MO = KC.MO(1)
SSHT = KC.LSFT(KC.LGUI(KC.S))
SCP = KC.LCTL(KC.LSFT(KC.C))
SPT = KC.LCTL(KC.LSFT(KC.V))


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

GTGL = Key(on_press=toggle_game_layer)
#keymap


keyboard.keymap = [
    [KC.N1,   KC.N2,   KC.N3,   KC.N4,  KC.N5,       KC.N6,   KC.N7,  KC.N8,   KC.N9,    KC.N0,
     KC.Q,    KC.W,    KC.E,    KC.R,   KC.T,        KC.Y,    KC.U,   KC.I,    KC.O,     KC.P,
     KC.A,    KC.S,    KC.D,    KC.F,   KC.G,        KC.H,    KC.J,   KC.K,    KC.L,     KC.SCLN,
     KC.Z,    KC.X,    KC.C,    KC.V,   KC.B,        KC.N,    KC.M,   KC.COMM, KC.DOT,   KC.SLSH,
     KC.LSFT, KC.LALT, KC.LCTL, KC.SPC, KC.RCMD,     KC.RSFT, MO,     KC.ENT,  KC.MINS,  KC.EQL],

    [KC.F1,   KC.F2,   KC.F3,   KC.F4,  KC.F5,       KC.F6,   KC.F7,  KC.F8,   KC.F9,    KC.F10,
     KC.ESC,  KC.TILD, KC.UP,   KC.NO,  KC.NO,       KC.LBRC, KC.RBRC,KC.BSLS, KC.LPRN,  KC.RPRN,
     KC.MPLY, KC.LEFT, KC.DOWN, KC.RGHT,KC.NO,       SSHT,    KC.NO,  KC.NO,   KC.NO,    KC.QUOT,
     KC.MPRV, KC.MNXT, SCP,     SPT,    KC.NO,       KC.CAPS, KC.NO,  KC.NO,   KC.NO,    KC.NO,
     KC.LSFT, KC.NO,   KC.NO,   KC.TAB, KC.BSPC,     KC.RSFT, MO,     GTGL,    KC.UNDS,  KC.PLUS],

    [KC.N1,   KC.N2,   KC.N3,   KC.N4,  KC.N5,       KC.ESC,  KC.TAB, KC.F12,  KC.F1,    KC.F2,
     KC.N5,   KC.Q,    KC.W,    KC.E,   KC.R,        KC.NO,   KC.NO,  KC.NO,   KC.NO,    KC.NO,
     KC.LSFT, KC.A,    KC.S,    KC.D,   KC.F,        KC.NO,   KC.NO,  KC.NO,   KC.NO,    KC.NO,
     KC.LCTL, KC.Z,    KC.X,    KC.C,   KC.V,        KC.NO,   KC.NO,  KC.NO,   KC.NO,    KC.NO,
     KC.SPC,  KC.SPC,  KC.SPC,  KC.SPC, KC.SPC,      KC.NO,   KC.NO,  GTGL,    KC.NO,    KC.NO]





]
if __name__ == "__main__":
    keyboard.go()


