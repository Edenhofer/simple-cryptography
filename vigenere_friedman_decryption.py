#!/usr/bin/env python
import ABC
import mymod
import math
import sys

# Requesting name of textfile
print("Name der Textdatei:")
textfilename=input()
text=ABC.getTextfile(textfilename)

# Transform Text to Numbers
textNum=ABC.transformTextToNum(text)
m=len(textNum)

temp=mymod.fa(textfilename)
textcount=temp[1]
sigma=0
# Loop for summing up sigma
for i in range(0, len(textcount)):
	sigma+=textcount[i]*(textcount[i]-1)

# Calculating the Coincidence Index	
coindex=sigma/(m*(m-1))

# Calculating passphrase length
coindexger=0.0762
coindexran=0.0385
k=((coindexger-coindexran)*m)/((m-1)*coindex-coindexran*m+coindexger)
if k < 0: k *= -1
print("Die Schlüssellänge beträgt ca.:", int(round(k, 0)),"(",k,") Zeichen.")
k=int(round(k, 0))

# Genrating the key for k, k+1 and k-1
for k in range(k-1, k+2):
	# Splitting the text into several blocks, which are encrypted with Caesar
	result=[]
	# numbercount=[]
	for v in range(0, k):
		resultcount=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]	# Counter for the letters
		frequentletterlist=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
		temp=0
		
		i=v
		while i<len(textNum):
			resultcount[textNum[i]]+=1
			i+=k
		
		for u in range(0, len(resultcount)):
			for i in range(0, len(resultcount)):
				n=i+1
				if n>=len(resultcount): n-=1
				if resultcount[frequentletterlist[i]]<resultcount[frequentletterlist[n]]:
					temp=frequentletterlist[i]
					frequentletterlist[i]=frequentletterlist[n]
					frequentletterlist[n]=temp		
				
		result.append(frequentletterlist)
		# numbercount.append(resultcount)
	
	# Calculating key
	keyi=[]
	keys=[]
	frequentletter=[]
	for i in range(0, k):
		frequentletter=result[i]
		# count=numbercount[i]
		keyi.extend([(frequentletter[1]-frequentletter[0])*3%26])
		keys.extend([(frequentletter[0]-keyi[i]*4)%26])
	
	print("Der Schlüssel lautet: \"",ABC.transformNumToText(keys),"\"\tfür k=",k)
