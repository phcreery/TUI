# TUI
Simple Text/Terminal User Interface library and can be used for devices with limited capabilities

## Getting Started

I know that several TUI exist, like curses, asciimatics, urwid, npyscreen, etc but none seemed to have what I needed so I made my own.

### Prerequisites

NONE

### Installing

```
git clone "https://github.com/phcreery/TUI.git"
```

## Running

Be sure the kbd.py is in the same directory. It is the library
```
sudo python3 main.py
```

### Usage

Currently there is only one thing it does and is pretty limited but this has big dreams
```
kbd.tuiinput("Title",(width,height),"big/small/tiny","inital text","Tooltip")
```
This displays a textbox with an onscreen QWERTY keyboard that is operated using the WASD keys. The keyboard is changed with R & F keys. Keypress is simulted with E key. Q breaks the script.

![](images/screenshot2.png)


## ToDo
This is the list of future changes:

 - [ ] Organize library directory with folder heirarchy
 - [ ] More "Modules"/Libraries
 - [ ] Text boxes
 - [ ] Buttons


## Authors

* **Peyton Creery** - *Initial work* 
