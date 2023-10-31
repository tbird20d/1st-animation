def on_forever():
    basic.show_string("I am Tim!!")
    basic.show_icon(IconNames.SCISSORS)
    basic.pause(1000)
    basic.show_string("  ")
basic.forever(on_forever)
