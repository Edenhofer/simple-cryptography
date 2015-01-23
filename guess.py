#!/usr/bin/env python
import random
import math

def guessing():
	ran=random.randint(1, 100)
	guess=-1
	print("Errate die zufällig generierte Zahl(1-100).")

	while True:
		guess=int(input())
		if guess==ran:
			print("Juhu du hast richtig getippt!! :D")
			break
		elif guess<ran: print("Deine Eingabe ist geringer als random")
		elif guess>ran: print("Deine Eingabe ist größer als random")
		
guessing()
