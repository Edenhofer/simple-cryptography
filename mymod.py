#!/usr/bin/env python
import math
import sys
import random
import string
import os

# Greatest common divisor
def gcd(a, b):
	if a == b: return a
	while b > 0: a, b = b, a % b
	return a

# Lowest common multiplier
def lcm(a, b):
	return abs(a * b) // gcd(a, b)
	
# Extended euclidean algorythm
def eec(a, b):
	u, v, s, t = 1, 0, 0, 1
	while b > 0:
		q = a//b
		a, b = b, a-q*b
		u, s = s, u-q*s
		v, t = t, v-q*t
		
	result = [a, u, v]
	return result

"""
# Recursive Funtion for the extended euclidean algorythm
def eec(a, b):
	if b==0:
		return [a, 1, 0]
	else:
		z=eec(b, a%b)
		# z[0] is the greatest common divisor, z[sth.] is s or t (depends on the order of the input)
		return [z[0], z[2], z[1]-(a//b)*z[2]]
"""

# Faculty	
def faculty(x):
	y=1
		
	for i in range(1, x+1):
		y*=i

	return(y)
	
# Efficient exponentiation (a^b)%N
def ee(x, k, N = 0):
	result = 1
	exp = x
	
	# In case N is set and modulo calculation is required
	if N != 0:
		while k > 0:
			if k % 2 == 1: result = result * exp % N
			exp = exp * exp % N
			k = k // 2

	# In case no N is given
	else: 
		while k > 0:
			if k % 2 == 1: result = result * exp
			exp = exp * exp
			k = k // 2
	
	return result

# Frequency Analysis
def fa(textfile):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	filesystem = "Texte/"					# Folder for the textfile
	resultcount = [0 for x in range(26)]			# Counter for the letters
	resultper = resultcount					# Percentage of each letter
	frequentletterlist = [x for x in range(26)]
	temp = 0
	
	# Getting textfile and putting its content in text
	text =""
	try:
		fobj= open(filesystem + textfile + ".txt")
		for line in fobj:
			text += line.rstrip()
		fobj.close()
	except IOError:
		print("Diese Textdatei existiert nicht.")
		os._exit(1)
	
	# Transforming the text into numbers
	textnum = []
	text = text.lower()
	for buchstabe in text:
		if buchstabe in string.ascii_letters: 
			zahl = (int(alphabet.index(buchstabe)))%26
			textnum.append(zahl)
	
	# Counting the frequency of each number
	for i in range(0, len(textnum)):
		resultcount[textnum[i]]+=1
	
	# Sorting the frequency of each letter in descending order
	for u in range(0, len(resultcount)):
		for i in range(0, len(resultcount)):
			n=i+1
			if n>=len(resultcount): n-=1
			if resultcount[frequentletterlist[i]]<resultcount[frequentletterlist[n]]:
				temp=frequentletterlist[i]
				frequentletterlist[i]=frequentletterlist[n]
				frequentletterlist[n]=temp		
	
	# Calculating the frequency of each letter in percent		
	for i in range(0, len(resultcount)):
		resultper[i]=resultcount[i]/len(textnum)*100
		
	result=[frequentletterlist, resultcount, resultper]
	return(result)
	
# Calculating Primes below the input N
def primesbelow(N):
	# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
	#""" Input N>=6, Returns a list of primes, 2 <= p < N """
	correction = N % 6 > 1
	N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
	sieve = [True] * (N // 3)
	sieve[0] = False
	for i in range(int(N ** .5) // 3 + 1):
		if sieve[i]:
			k = (3 * i + 1) | 1
			sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
			sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
	return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]

# Check whether the input is a prime
smallprimeset = set(primesbelow(100000))
_smallprimeset = 100000
def isprime(n, precision=7):
	# http://en.wikipedia.org/wiki/Miller-Rabin_primality_test#Algorithm_and_running_time
	if n == 1 or n % 2 == 0:
		return False
	elif n < 1:
		raise ValueError("Out of bounds, first argument must be > 0")
	elif n < _smallprimeset:
		return n in smallprimeset


	d = n - 1
	s = 0
	while d % 2 == 0:
		d //= 2
		s += 1

	for repeat in range(precision):
		a = random.randrange(2, n - 2)
		x = pow(a, d, n)

		if x == 1 or x == n - 1: continue

		for r in range(s - 1):
			x = pow(x, 2, n)
			if x == 1: return False
			if x == n - 1: break
		else: return False

	return True

# https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
def pollard_brent(n):
	if n % 2 == 0: return 2
	if n % 3 == 0: return 3

	y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
	g, r, q = 1, 1, 1
	while g == 1:
		x = y
		for i in range(r):
			y = (pow(y, 2, n) + c) % n

		k = 0
		while k < r and g==1:
			ys = y
			for i in range(min(m, r-k)):
				y = (pow(y, 2, n) + c) % n
				q = q * abs(x-y) % n
			g = gcd(q, n)
			k += m
		r *= 2
	if g == n:
		while True:
			ys = (pow(ys, 2, n) + c) % n
			g = gcd(abs(x - ys), n)
			if g > 1:
				break

	return g

# Claculating all primefactors of the input n
smallprimes = primesbelow(1000) # might seem low, but 1000*1000 = 1000000, so this will fully factor every composite < 1000000
def primefactors(n, sort=False):
	factors = []

	limit = int(n ** .5) + 1
	for checker in smallprimes:
		if checker > limit: break
		while n % checker == 0:
			factors.append(checker)
			n //= checker
			limit = int(n ** .5) + 1
			if checker > limit: break

	if n < 2: return factors

	while n > 1:
		if isprime(n):
			factors.append(n)
			break
		factor = pollard_brent(n) # trial division did not fully factor, switch to pollard-brent
		factors.extend(primefactors(factor)) # recurse to factor the not necessarily prime factor returned by pollard-brent
		n //= factor

	if sort: factors.sort()

	return factors

# Factorization
def factorization(n):
	factors = {}
	for p1 in primefactors(n):
		try:
			factors[p1] += 1
		except KeyError:
			factors[p1] = 1
	return factors

# Totients
totients = {}
def totient(n):
	if n == 0: return 1

	try: return totients[n]
	except KeyError: pass

	tot = 1
	for p, exp in factorization(n).items():
		tot *= (p - 1)  *  p ** (exp - 1)

	totients[n] = tot
	return tot
