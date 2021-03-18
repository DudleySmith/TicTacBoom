def on_button_pressed_a():
    RelancerCompteur()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    if receivedString.compare("Relancer") == 0:
        RelancerCompteur()
radio.on_received_string(on_received_string)

def on_gesture_shake():
    radio.send_string("Relancer")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def RelancerCompteur():
    global Compteur
    Compteur = randint(7, 15)
Compteur = 0
radio.set_group(1)
RelancerCompteur()

def on_forever():
    global Compteur
    basic.pause(1000)
    Compteur += -1
basic.forever(on_forever)

def on_forever2():
    if Compteur > 0:
        basic.show_number(Compteur)
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        music.play_tone(330, music.beat(BeatFraction.QUARTER))
    elif Compteur == 0:
        basic.show_leds("""
            . # # # .
                        # . . . #
                        # . . . #
                        . # . # .
                        . # . # .
        """)
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(196, music.beat(BeatFraction.HALF))
        music.play_tone(165, music.beat(BeatFraction.HALF))
        music.play_tone(131, music.beat(BeatFraction.BREVE))
    else:
        pass
basic.forever(on_forever2)
