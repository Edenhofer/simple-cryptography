#!/usr/bin/env python
import math
import sys
import ABC
import mymod

# Hole Text
text=ABC.getText()

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
	TextNum[i]=TextNum[i]*keyi+keys
	
# Transformiere Zahlen und Text
text=ABC.transformNumToText(TextNum)

#Speichere Text
ABC.saveTextfile(text)
