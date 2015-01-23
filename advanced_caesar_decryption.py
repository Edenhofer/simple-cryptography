#!/usr/bin/env python
import math
import sys
import ABC
import mymod

# Abfrage des Namen der Textdatei
print("Name der Textdatei:")
textfilename=input()
text=ABC.getTextfile(textfilename)

# Hole Schlüssel
keyi=ABC.getKey()
if mymod.gcd(keyi, 26)!=1:
	print("Der Verschlüsselungalgorithmus muss umkehrbar sein: Die Zahl muss teilerfremd mit 26 sein.")
	sys.exit(0)
keys=ABC.getKey()

# Transformiere Text zu Zahlen
TextNum=ABC.transformTextToNum(text)

# Schleife
for i in range(0, len(TextNum)):
	TextNum[i]=(TextNum[i]-keys)%26
	while TextNum[i]%keyi!=0: TextNum[i]+=26
	TextNum[i]=int(TextNum[i]/keyi)
	if TextNum[i]<0: TextNum[i]*=-1
	
# Transformiere Zahlen und Text
text=ABC.transformNumToText(TextNum)

# Speichere Text
print(text)
