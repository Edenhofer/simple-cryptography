#!/usr/bin/env python
import math
import sys
import mymod

# Get key
print("Name der Datei für den privaten Schlüssel:")
textfile = input()
temp = ""
try:
	fobj = open("keys/"+ textfile + "")
	for line in fobj:
		temp += line.rstrip()
	fobj.close()
except IOError:
	print("Diese Datei existiert nicht.")
	exit()

# Getting the variables for the decryption: d, N, phi, p and q
d = N = phi = p = q =""
n = 0
for i in range(1, (len(temp)-1)):
	if temp[i] is not " ":
		if temp[i] is ",": n += 1
		elif n == 0: d += temp[i]
		elif n == 1: N += temp[i]
		elif n == 2: phi += temp[i]
		elif n == 3: p += temp[i]
		elif n == 4: q += temp[i]	
d = int(d)
N = int(N)
phi = int(phi)
p = int(p)
q = int(q)

# Getting the blocklength
print("Mit welcher Blockgröße wurde der Text verschlüsselt?")
blocksize = input()

# Getting the cyphertext
print("Name der zu entschlüsselnden Datei:")
textfile = input()
temp = ""
try:
	fobj = open("output/"+ textfile + "_crypt")
	for line in fobj:
		temp += line.rstrip()
	fobj.close()
except IOError:
	print("Diese Datei existiert nicht.")
	exit()
n = 0
for i in range(0, len(temp)):
	if temp[i] is "," or temp[i] is "[" or temp[i] is "]": n +=1
num = ["" for x in range(n)]
n = 0
for i in range(1, (len(temp)-1)):
	if temp[i] is not " ":
		if temp[i] is "[" or temp[i] is "]" or temp[i] is ",": n += 1
		else: num[n] += temp[i]

num = [x for x in num if x is not ""]
num = [int(num[x]) for x in range(len(num))]

# Transform text to numbers
# Until now there the cypher is not transformed to text
# num = [ord(c) for c in text]

# Splitting text into blocks
""" Hier fehlt noch wat!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""

# Decryption loop
for i in range(0, len(num)):
	num[i] = mymod.ee(num[i], d, N)

# Calculating and displaying plain text
text = ""
print(num)
for i in range(0, len(num)): text += chr(num[i])
print("Der Klartext lautet: \n",text)
