'''
This is an example script to showcase TUI
'''

import tui.general
import tui.kbd
import os
import subprocess


screensize = tui.general.getsize()

r = tui.kbd.kbdinput("Prompt",screensize,"small","")

print(r)
