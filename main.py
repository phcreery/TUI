'''
This is an example script to showcase TUI
'''

import tui

screensize = tui.general.getsize()

r = tui.kbdinput("Prompt",screensize,"small","")

print(r)
