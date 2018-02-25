#! python3
#mapIt.py - Lunches a map in the browsser using an address from the
#command line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #Get address from command line.
    # argvs = sys.argv
    address = ' '.join(sys.argv[1:])
# print(argvs)
# print(address)
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&q=' + address)

