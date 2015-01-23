#!/usr/bin/env python
import math
import random
import sys
import mymod

# Smallest allowed size of N
mini=100
# Maximum size of e
maxi=1000

# Getting the primes
print("1. Primzahl?")
p = int(input())
if mymod.isprime(p) is False and p != 2:
	print(p, "ist keine Primzahl.")
	exit()
print("2. Primzahl?")
q = int(input())
if mymod.isprime(q) is False and q != 2:
	print(q, "ist keine Primzahl.")
	exit()
if p == q:
	print("Die Primzahlen dürfen nicht gleich sein.")
	exit()

# Calculating N and phi and checking for some weaknesses	
N = p*q
phi = (p-1)*(q-1)
if N <= mini:
	print(N, "ist kleiner als die mindestens gefordert Schlüssellänge (", mini, ").")
	exit()
if p>q: p, q = q, p

# Calculating e
while True:
	if N<1000: maxi = N-1
	e = random.randint(mini, maxi)
	if mymod.gcd(phi, e) == 1 and e != p and e != q: break

print("Unter welchem Namen soll der Schlüssel gespeichert werden?")		
# Saving the public key
key = str([N, e])
name = input()
fobj_out = open("keys/"+ name + ".pub","w")
for i in range(int(len(key)/32)+1):
	for k in range(4):
		for j in range(8):
			try:
				fobj_out.write(key[32*i+8*k+j])
			except IndexError:
				fobj_out.write(' ')
		fobj_out.write(' ')
	fobj_out.write('\n')
fobj_out.close()

# Getting the inverse of e := calculating d
temp = mymod.eec(e, phi)
d = (temp[1]%phi)

# Saving the private key
key = str([d, N, phi, p, q])
fobj_out = open("keys/"+ name + "","w")
for i in range(int(len(key)/32)+1):
	for k in range(4):
		for j in range(8):
			try:
				fobj_out.write(key[32*i+8*k+j])
			except IndexError:
				fobj_out.write(' ')
		fobj_out.write(' ')
	fobj_out.write('\n')
fobj_out.close()
