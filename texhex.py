'''
How to Convert Text to Hex

Get character.
Get decimal code of character from ASCII table.
Convert decimal to hex byte.
Continue with next character.
'''

def txhx(tx:str):
    hx = ''
    for c in tx:
        dec = ord(c)
        hx += hex(dec)[2:]
    print(hx)  

  