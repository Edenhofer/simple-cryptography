#!/usr/bin/env python
import math
import ABC

# Abfrage des Namen der Textdatei
print("Name der Textdatei:")
textfilename=input()
text=ABC.getTextfile(textfilename)

# Hole Schlüssel
key=ABC.getKey()

# Transformiere Text zu Zahlen
TextNum=ABC.transformTextToNum(text)

# Schleife
for i in range(0, len(TextNum)):
	TextNum[i]-=key
	
# Transformiere Zahlen und Text
text=ABC.transformNumToText(TextNum)

# Speichere Text
print(text)
