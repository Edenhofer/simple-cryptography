#!/usr/bin/env python
import math
import sys
import ABC

# Abfrage des Namen der Textdatei
print("Name der Textdatei:")
textfilename=input()
text=ABC.getTextfile(textfilename)

# Hole Schlüssel
print("Schlüssel(Wort)?")
keys=input()
key=ABC.transformTextToNum(keys)

# Transformiere Text zu Zahlen
TextNum=ABC.transformTextToNum(text)

# Schleife
for i in range(0, len(TextNum)):
	TextNum[i]=TextNum[i]-key[i%len(key)]
	
# Transformiere Zahlen und Text
text=ABC.transformNumToText(TextNum)

# Speichere Text
print(text)
