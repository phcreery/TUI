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
        print("".join(" " for x in range(0, int(round((width-20)/2)-0.001) )), end="")
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
        print("".join(" " for x in range(0, int(round((width-20)/2)-0.001) )), end="")
        for col in range(0,len(keyarray[0])):
            if (col == keyx) & (row == keyy):
                print(CRED + keyarray[row][col] + CEND, end="")
            else:
                print(keyarray[row][col], end="")
        print("\n", end="")
    #print()
    

def drawkbdbig(keyx,keyy, keyarray, width):
    
    for row in range(0,len(keyarray)):
        print("".join(" " for x in range(0, int(round((width-30)/2)-0.001) )), end="")
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


def getinput(x,y,z):
    char = getch()
    a=0
    if (char == "p"):
        print("Stop!")
        exit(0)
        
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
    elif (char == "q"):
        a=1
        
    return(x,y,z,a)


def tuiinput(title,width,height,size,keystr):
    global x,y,z,a
    while len(keystr)<30:
        os.system("clear")
        #x = random.randint(0, len(keyarray[0][0])-1)
        #y = random.randint(0, len(keyarray[0])-1)
        #z = random.randint(0, len(keyarray)-1)
        
        
        
        print("".join("\n" for x in range(0, int(round((height-7)/2)-0.001) )), end="")
        drawtxtbox(title, keystr, width)
        print("".join("\n" for x in range(0, int(round((height-7)/2)-0.001) )), end="")
        #print()
        if size == "big":
            drawkbdbig(x,y, keyarray[z], width)
        elif size == "small":
            drawkbd(x,y, keyarray[z], width)
        elif size == "tiny":
            drawkbdtiny(x,y, keyarray[z], width)
    
        x,y,z,a = getinput(x,y,z)
        
        x = clamp(x, 0, len(keyarray[0][0])-1)
        y = clamp(y, 0, len(keyarray[0])-1)
        z = clamp(z, 0, len(keyarray)-1)
        
        if a == 1:
            keystr = keystr + keyarray[z][y][x]
    
        

"""
while len(keystr)<30:
    os.system("clear")
    x = random.randint(0, len(keyarray[0][0])-1)
    y = random.randint(0, len(keyarray[0])-1)
    z = random.randint(0, len(keyarray)-1)
    keystr = keystr + keyarray[z][y][x]
    drawtxtbox(keystr)
    print()
    drawkbdbig(x,y, keyarray[z])
    time.sleep(0.5)
    """
