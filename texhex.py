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
    return hx  

# importing required modules
import argparse

# create a parser object
parser = argparse.ArgumentParser(description = "A text to hex converter")

# add argument
parser.add_argument("txhx", nargs = '*', metavar = "txhx", type = str,
					help = "gimme text i give u hex")

# parse the arguments from standard input
args = parser.parse_args()

# check if add argument has any input data.
# If it has, then print sum of the given numbers
output = ''
if len(args.txhx) != 0:
    for word in args.txhx:
	    output += txhx(word) + ' '
print(output)

  