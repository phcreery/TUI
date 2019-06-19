import os
import time
import random
import sys, termios, tty

#width = 40
#title="User:"

keyarray1 = [['1','2','3','4','5','6','7','8','9','0'],
             ['q','w','e','r','t','y','u','i','o','p'],
             ['a','s','d','f','g','h','j','k','l',';'],
             ['z','x','c','v','b','n','m',' ','.','/']]

keyarray2 = [['1','2','3','4','5','6','7','8','9','0'],
             ['Q','W','E','R','T','Y','U','I','O','P'],
             ['A','S','D','F','G','H','J','K','L',':'],
             ['Z','X','C','V','B','N','M',' ',',','\\']]

keyarray3 = [['!','@','#','$','%','^','&','*','(',')'],
             ['~',' ',' ',' ','_','+','-','=','{','}'],
             ['`',' ',' ',' ',',','\"','\'','?','[',']'],
             [' ',' ',' ',' ',' ',' ','<','>','|',' ']]            
keyarray = [keyarray1,keyarray2,keyarray3]

keystr = ""
x=0
y=0
z=0
a=0
CRED = '\033[44m'
CEND = '\033[0m'

#print("Hello World")


def drawkbd(keyx,keyy, keyarray, width):
    for row in range(0,len(keyarray)):
        print("".join(" " for x in range(0, int(round((width-20)/2)) )), end="")
        for col in range(0,len(keyarray[0])):
            if (col == keyx) & (row == keyy):
                print("[", end="")
            elif (col == keyx+1) & (row == keyy):
                print("", end="")
            else:
                print(" ", end="")
            print(keyarray[row][col], end="")
            if (col == keyx) & (row == keyy):
                print("]", end="")
            else:
                print("", end="")
        print("\n", end="")
    #print()
    
    
def drawkbdtiny(keyx,keyy, keyarray, width):
    for row in range(0,len(keyarray)):
        print("".join(" " for x in range(0, int(round((width-20)/2)) )), end="")
        for col in range(0,len(keyarray[0])):
            if (col == keyx) & (row == keyy):
                print(CRED + keyarray[row][col] + CEND, end="")
            else:
                print(keyarray[row][col], end="")
        print("\n", end="")
    #print()
    

def drawkbdbig(keyx,keyy, keyarray, width):
    for row in range(0,len(keyarray)):
        print("".join(" " for x in range(0, int(round((width-30)/2)) )), end="")
        for col in range(0,len(keyarray[0])):
            if (col == keyx) & (row == keyy):
                print("[", end="")
            else:
                print(" ", end="")
            print(keyarray[row][col], end="")
            if (col == keyx) & (row == keyy):
                print("]", end="")
            else:
                print(" ", end="")
        print("\n", end="")
    #print()
    
def drawkbdgiant(keyx,keyy, keyarray, width):
    for row in range(0,2*len(keyarray)+1):
        print("".join(" " for x in range(0, int(round((width-30)/2)) )), end="")
        for col in range(0,len(keyarray[0])):
            
                
            if row % 2 == 1:
                
                if (col == keyx) & (round(row/2-0.01) == keyy):
                    print(u"\u2502", end="")
                else:
                    print(" ", end="")
                
                print(keyarray[round(row/2-0.01)][col], end="")
                
                if (col == keyx) & (round(row/2-0.01) == keyy):
                    print(u"\u2502", end="")
                else:
                    print(" ", end="")
                
            else:
                if (col == keyx):
                    if (round(row/2-0.01) == keyy):
                        print(u"\u250C", end="")
                        print(u"\u2500", end="")
                        print(u"\u2510", end="")
                    elif (round(row/2-0.01)-1 == keyy) :
                        print(u"\u2514", end="")
                        print(u"\u2500", end="")
                        print(u"\u2518", end="")
                
                else:
                    print("   ", end="")

                
        print("\n", end="")
    #print()

def drawtxtbox(title,data,width):
    data=data[-(width-4):]
    print(u'\u2554', end=" ")
    print(title, end=" ")
    print("".join(u'\u2550' for x in range(0,width-2-len(title)-2 )), end="")
    print(u'\u2557')
    #print("-----------------------------")
    print(u'\u2551', data, end="")
    print(u'\u2588', end="")
    print("".join(" " for x in range(0,(width-4)-len(data))), end="")
    print(u'\u2551')
    print(u'\u255A', end="")
    print("".join(u'\u2550' for x in range(0,width-2)), end="")
    print(u'\u255D')

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def getinput(x,y,z,kbd):
    char = getch()
    #kbd=True
    a=0
    if (char == "q"):
        #print("Stop!")
        kbd=False
        #exit(0)
        
    elif (char == "a"):
        x=x-1
    elif (char == "d"):
        x=x+1
    elif (char == "w"):
        y=y-1
    elif (char == "s"):
        y=y+1
    elif (char == "r"):
        z=z+1
    elif (char == "f"):
        z=z-1
    elif (char == "e"):
        a=1
    elif (char == "c"):
        a=-1
        
    return(x,y,z,a,kbd)



def initmanualkbdinput():
    a=0
    y=0
    z=0
    a=0
    kbd=True   
    return(x,y,z,a,kbd)

def setkbdinput(status,command):
    x,y,z,a,kbd = status
    #char = getch()
    #kbd=True
    a=0
    if (command == "exit"):
        #print("Stop!")
        kbd=False
        #exit(0)
        
    elif (command == "left"):
        x=x-1
    elif (command == "right"):
        x=x+1
    elif (command == "up"):
        y=y-1
    elif (command == "down"):
        y=y+1
    elif (command == "+"):
        z=z+1
    elif (command == "-"):
        z=z-1
    elif (command == "select"):
        a=1
    elif (command == "backspace"):
        a=-1
        
    return(x,y,z,a,kbd)

def drawkbdinput(title,dispsize,size,keystr,tooltip,status):
    x,y,z,a,kbd = status
    height, width = dispsize

    os.system("clear")
    #x = random.randint(0, len(keyarray[0][0])-1)
    #y = random.randint(0, len(keyarray[0])-1)
    #z = random.randint(0, len(keyarray)-1)
    
    #rows, columns = os.popen('stty size', 'r').read().split()
    #print("start")
    print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")
    drawtxtbox(title, keystr, width)
    print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")
    #print()
    if size == "big":
        drawkbdbig(x,y, keyarray[z], width)
    elif size == "small":
        drawkbd(x,y, keyarray[z], width)
    elif size == "tiny":
        drawkbdtiny(x,y, keyarray[z], width)
    elif size == "giant":
        drawkbdgiant(x,y, keyarray[z], width)
    
    print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")
    print("".join(" " for x in range(0, int(round((width-len(tooltip))/2)) )), end="")
    print(tooltip)
    #x,y,z,a,kbd = getinput(x,y,z,kbd)
    
    x = clamp(x, 0, len(keyarray[0][0])-1)
    y = clamp(y, 0, len(keyarray[0])-1)
    z = clamp(z, 0, len(keyarray)-1)
    
    if a == 1:
        keystr = keystr + keyarray[z][y][x]

    return(keystr)


def kbdinput(title,dispsize,size,keystr,tooltip):
    global x,y,z,a
    height, width = dispsize
    kbd=True
    while kbd == True:
        os.system("clear")
        #x = random.randint(0, len(keyarray[0][0])-1)
        #y = random.randint(0, len(keyarray[0])-1)
        #z = random.randint(0, len(keyarray)-1)
        
        #rows, columns = os.popen('stty size', 'r').read().split()
        #print("start")
        print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")
        drawtxtbox(title, keystr, width)
        print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")
        #print()
        if size == "big":
            drawkbdbig(x,y, keyarray[z], width)
        elif size == "small":
            drawkbd(x,y, keyarray[z], width)
        elif size == "tiny":
            drawkbdtiny(x,y, keyarray[z], width)
        elif size == "giant":
            drawkbdgiant(x,y, keyarray[z], width)
        
        print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")
        print("".join(" " for x in range(0, int(round((width-len(tooltip))/2)) )), end="")
        print(tooltip)
        x,y,z,a,kbd = getinput(x,y,z,kbd)
        
        x = clamp(x, 0, len(keyarray[0][0])-1)
        y = clamp(y, 0, len(keyarray[0])-1)
        z = clamp(z, 0, len(keyarray)-1)
        
        if a == 1:
            keystr = keystr + keyarray[z][y][x]
        elif a == -1:
            keystr = keystr[:-1]
    
    return(keystr)
        

if __name__ == '__main__':
    kbdinput("Prompt",40,13,"tiny","")
