'''
This is an demo script to showcase TUI
'''

import tui

screensize = tui.getsize()

def intrusive():
    # Launches Input and waits for user to complete the Input
    r = tui.kbdinput("Prompt",screensize,"small","","WASD to Move     E to select    C for backspace    R/F to change KBD     Q to quit")

    print(r)

def unintrusive():
    # Manual keyboard strokes and refreshing of Input
    manually = tui.manualkbdinput()
    manually.sendkbdinput("down")
    manually.sendkbdinput("right")
    manually.drawkbdinput("Prompt",screensize,"medium","","Unintrusive KBD")


#intrusive()
unintrusive()
