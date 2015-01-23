#!/usr/bin/env python
import math
import sys
import ABC
import mymod

# Demanding filename
print("Name der Textdatei:")
textfilename=input()
text=ABC.getTextfile(textfilename)

# Doing some frequency Analysis
fa=mymod.fa(textfilename)
fa_frequentletter=fa[0]
c_frequentletter=fa[1]

# Returning key
def genkey():
	keyi=(fa_frequentletter[1]-fa_frequentletter[0])*3%26
	keys=(fa_frequentletter[0]-keyi*4)%26
	
	# Printing Keys
	print("Key01: ", keyi, " Key02:", keys)

"""
# Searching for equaly frequent letter which are next to each other
x=4
for i in range(0, x):
	if c_frequentletter[fa_frequentletter[x]]==c_frequentletter[fa_frequentletter[x+1]]:
		genkey()
		temp1 = fa_frequentletter[x]
		temp2 = fa_frequentletter[x+1]
		fa_frequentletter[x] = fa_frequentletter[x+1]
		fa_frequentletter[x+1] = fa_frequentletter[x+2]
		genkey()
		fa_frequentletter[x] = temp1
		genkey()
		fa_frequentletter[x] = temp1
		fa_frequentletter[x] = temp2
"""
	
genkey()
