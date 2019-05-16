'''
This is an example script to showcase TUI
'''

import tui
import os

screensize = tui.general.getsize()

r = tui.kbdinput("Prompt",screensize,"small","")

print(r)
