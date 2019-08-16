# reverse your buffer text

import pyperclip

s = pyperclip.paste()
s = s[::-1]
pyperclip.copy(s)
