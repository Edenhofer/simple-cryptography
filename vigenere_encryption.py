#!/usr/bin/env python
import math
import sys
import ABC

# Hole Text
text=ABC.getText()

# Hole Schlüssel
print("Schlüssel(Wort)?")
keys=input()
key=ABC.transformTextToNum(keys)

# Transformiere Text zu Zahlen
TextNum=ABC.transformTextToNum(text)

# Schleife
for i in range(0, len(TextNum)):
	TextNum[i]=TextNum[i]+key[i%len(key)]
	
# Transformiere Zahlen und Text
text=ABC.transformNumToText(TextNum)

# Speichere Text
ABC.saveTextfile(text)
