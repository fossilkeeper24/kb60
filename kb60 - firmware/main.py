print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.extensions.international import International

from kmk.modules.layers import Layers

from kmk.extensions.media_keys import MediaKeys

from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14,)
keyboard.row_pins = (board.GP15, board.GP16, board.GP17, board.GP18, board.GP19,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(International())
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())
keyboard.modules = [layers, holdtap, encoder_handler]

TRANS = KC.TRNS
xxxxxxx = KC.NO
RAISE = KC.KC.TT(1)

keyboard.keymap = [
        [ #LAYER 0: BASE
        KC.GESC, KC.1,    KC.2,    KC.3,    KC.4,    KC.5,    KC.6,    KC.7,    KC.8,    KC.9,    KC.0,    KC.MINS, KC.EQL,  KC.BSPC, KC.MUTE, 
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.NUHS, KC.MPLY,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.NO,   KC.QUOT, KC.ENT,  KC.MUTE,
        KC.LSFT, KC.NUBS, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.UP,   KC.PSCR,
        KC.LCTL, KC.LGUI, KC.LALT, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.NO,   KC.NO,   KC.RALT, RAISE,   KC.LEFT, KC.DOWN, KC.RGHT,]
        [ #LAYER 1: FN
        KC.GESC, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,    KC.DELETE, KC.GRV,
        TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,     TRANS,     TRANS,
        TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   KC.NO,   TRANS,     TRANS,     TRANS,
        TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,     KC.PGUP,   TRANS,
        TRANS,   TRANS,   TRANS,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   TRANS,   KC.NO,   KC.NO,   TRANS,   TRANS,   KC.HOME,   KC.PGDN,   KC.END,]]

encoder_handler.divisor = 2
encoder_handler.pins = ((board.GP21, board.GP22, None,), )

encoder_handler.map = [ (( KC.VOLD, KC.VOLU,),), # Layer 0
                        (( KC.BRID, KC.BRIU,),), ] # Layer 1

if __name__ == '__main__':
    keyboard.go()

'''  [KC.ESC, KC.1,    KC.2,    KC.3,    KC.4,    KC.5,    KC.6,    KC.7,    KC.8,    KC.9,    KC.0,    KC.MINS, KC.EQL,  KC.BSPC, KC.GRV,]
        [KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.NUHS, KC.NO,]
        [KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.NUHS, KC.ENT,]
        [KC.LSFT, KC.NUBS, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.RSFT, KC.UP,   KC.SLSH, KC.PSCR,]
        [KC.LCTL, KC.LGUI, KC.LALT, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.NO,   KC.RALT, KC.RGUI, KC.LEFT, KC.DOWN, KC.RGHT]

'''