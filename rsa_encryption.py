#!/usr/bin/env python
import math
import sys
import mymod

# Get key
print("Name der Datei für den öffentlichen Schlüssel:")
textfile = input()
temp = ""
try:
	fobj = open("keys/"+ textfile + ".pub")
	for line in fobj:
		temp += line.rstrip()
	fobj.close()
except IOError:
	print("Diese Datei existiert nicht.")
	exit()

# Getting N and e
N = e = ""
n = 0
for i in range(1, (len(temp)-1)):
	if temp[i] is not " ":
		if temp[i] is not "," and n == 0: N += temp[i]
		elif n == 1: e += temp[i]
		else: n = 1

N = int(N)
e = int(e)

# Getting the blocklength
print("Mit welcher Blockgröße soll der Text verschlüsselt werden?")
blocksize = input()
if blocksize is "":
	print("Es muss eine Blocklänge angegeben werden.")
	exit()
blocksize = int(blocksize)

print("Bitte zu verschlüsselnden Klartext eingeben:")
text = input()

# Transform text to numbers
num = [ord(c) for c in text]

# Check wether the input is coprime
#for i in range(0, len(num)):
#	if mymod.gcd(N, num[i]) != 1:
#		print("Die Eingabe kann aus Sicherheitsgründen nicht versschlüsselt werden.")
#		exit()


# Splitting text into blocks
# Defining the how many blocks are needed
if len(num)%blocksize == 0: strnum = ["" for x in range((len(num)//blocksize))]
else: strnum = ["" for x in range((len(num)//blocksize)+1)]

print("NUM: ", len(num))
print("STRNUM: ", len(strnum))

z = 0
while i < len(num):
	for n in range(0, blocksize):
		if i + n >= len(num): break
		strnum[z] += str(num[i+n])
	
	i += blocksize
	z += 1
	
print(strnum)
""" Hier fehlt noch wat!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""

# Encryption loop
for i in range(0, len(num)):
	num[i] = mymod.ee(num[i], e, N)

# Calculating cryptic text
# text = [chr(c) for c in num]
text = str(num)

# Save file
print("Unter welchem Namen soll der Text gespeichert werden?")
name = input()
fobj_out = open("output/"+ name + "_crypt","w")
for i in range(int(len(text)/32)+1):
	for k in range(4):
		for j in range(8):
			try:
				fobj_out.write(text[32*i+8*k+j])
			except IndexError:
				fobj_out.write(' ')	# Exit loop
		fobj_out.write(' ')
	fobj_out.write('\n')
fobj_out.close()
