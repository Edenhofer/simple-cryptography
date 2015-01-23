#!/usr/bin/env python
import math
import ABC

# Hole Text
text=ABC.getText()

# Hole Schlüssel
key=ABC.getKey()

# Transformiere Text zu Zahlen
TextNum=ABC.transformTextToNum(text)

# Schleife
for i in range(0, len(TextNum)):
	TextNum[i]+=key
	
# Transformiere Zahlen und Text
text=ABC.transformNumToText(TextNum)

#Speichere Text
ABC.saveTextfile(text)
