input.onButtonPressed(Button.A, function () {
    RelancerCompteur()
})
radio.onReceivedString(function (receivedString) {
    if (receivedString.compare("Relancer") == 0) {
        RelancerCompteur()
    }
})
input.onGesture(Gesture.Shake, function () {
    radio.sendString("Relancer")
})
function RelancerCompteur () {
    Compteur = randint(7, 15)
}
let Compteur = 0
radio.setGroup(1)
RelancerCompteur()
basic.forever(function () {
    if (Compteur > 0) {
        basic.showNumber(Compteur)
        music.playTone(262, music.beat(BeatFraction.Quarter))
        music.playTone(330, music.beat(BeatFraction.Quarter))
    } else if (Compteur == 0) {
        basic.showLeds(`
            . # # # .
            # . . . #
            # . . . #
            . # . # .
            . # . # .
            `)
        music.playTone(262, music.beat(BeatFraction.Half))
        music.playTone(196, music.beat(BeatFraction.Half))
        music.playTone(165, music.beat(BeatFraction.Half))
        music.playTone(131, music.beat(BeatFraction.Breve))
    } else {
    	
    }
})
basic.forever(function () {
    basic.pause(1000)
    Compteur += -1
})
