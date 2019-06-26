'''
This is an demo script to showcase TUI
'''

import tui

screensize = tui.getsize()


def getinput():
    char = tui.getch()
    if (char == "q"):
        press = "exit"
    elif (char == "a"):
        press = "left"
    elif (char == "d"):
        press = "right"    
    elif (char == "s"):
        press = "down"
    elif (char == "w"):
        press = "up"
    elif (char == "r"):
        press = "next"
    elif (char == "f"):
        press = "previous"
    elif (char == "c"):
        press = "back"
    elif (char == "e"):
        press = "select"
    return(press)

def intrusivekbd():
    # Launches Input and waits for user to complete the Input.
    # "defaultinput" sets input interpreter to library default
    # sizes: small/medium/big/giant
    r = tui.kbdinput("Prompt",screensize,"big","","WASD to Move     E to select    C for backspace    R/F to change KBD     Q to quit","defaultinput")

    print(r)

def unintrusivekbd():
    # Manual keyboard strokes and refreshing of Input
    manually = tui.manualkbdinput()
    manually.sendkbdinput("down")
    manually.sendkbdinput("right")
    manually.sendkbdinput("select")
    manually.sendkbdtext("asd")
    s = manually.drawkbdinput("Prompt",screensize,"medium","Unintrusive Keyboard")
    
    print(s)

def intrusivelist():
    #List box with user defined interperetation of input
    options = ["first","second","third","fourth"]
    t = tui.listselect("Select one:",screensize,options,"small","tooltip",getinput)
    print(t)



intrusivekbd()
#unintrusivekbd()
#intrusivelist()
