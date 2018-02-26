#! python3
#mapIt.py - Lunches a map in the browsser using an address from the
#command line or clipboard.

import webbrowser, sys, pyperclip

print("Please input your search word. If you want to set the source or the author, please input those factors after author: or  source:")

if len(sys.argv) > 1:
    #Get search words from command line.
    search_words = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    search_words = pyperclip.paste()

if sys.argv[-1] == 1:
    print("True")
    webbrowser.open('https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&q=%22' + search_words + "%22" )
    webbrowser.open('https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&q=' + search_words)
else:
    webbrowser.open('https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&q=' + search_words)

