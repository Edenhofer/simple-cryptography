#####################
#
#	Methodensammlung für Kurs 5.1 Hilden 2014
#
#	cge 2014_06_22  (1) getText():              Einlesen einer Texteingabe in einen String
#                   (2) getTextfile():          Einlesen einer Textdatei in einen String
#                   (3) getKey():               Wahl des Schlüssels - Caesar
#                   (4) transformTextToNum(str):    Umwandlung eines String in ein Zahlenliste gemäß 26-stelligem Alphabet
#
#                   (6) transformNumToText([int]):  Umwandlung einer Zahlenliste in String gemäß 26-stelligem Alphabet
#                   (7) saveTextfile(str):      Speichern eines Strings in einer Textdatei
#
#
#####################
	
import string
import os

alphabet = "abcdefghijklmnopqrstuvwxyz"

#Methoden
#1: Texteingabe wird in string gespeichert.
def getText(): 
    print("Bitte zu verschluesselnden Klartext eingeben:")
    Text = input()
    return Text
#2: Textdatei wird in string eingelesen.
def getTextfile(Name):
    Text =""
    try:
        fobj= open("Texte/"+Name + ".txt")
        for line in fobj:
            Text += line.rstrip()
        fobj.close()
        return Text
    except IOError:
        print("Diese Textdatei existiert nicht.")
        os._exit(1)
#3: Einlesen des Schluessels
def getKey():
    print("Schluessel(Zahl)?")
    try:
        Schluessel = int(input())
        return Schluessel
    except ValueError:
         print("hoppala, das war keine ganze Zahl")
         os._exit(1)
#4: Umwandeln eines Strings in eine Liste von Zahlen
def transformTextToNum(Text):
    Zahlenliste = []
    Text = Text.lower()
    for buchstabe in Text:
        if buchstabe in string.ascii_letters: 
            zahl = (int(alphabet.index(buchstabe)))%26
            Zahlenliste.append(zahl)
    return Zahlenliste

#6: Umwandeln von Zahlenliste in String
def transformNumToText(Zahlenliste):
    Text = ""
    for i in range(len(Zahlenliste)):
        zahl = (Zahlenliste[i])%26
        Text += alphabet[zahl]
    return Text
#7: Erzeugen einer Textfile, welche den angegebenen String enthaelt.
def saveTextfile(Text):
    print("Unter welchem Namen soll der Text gespeichert werden?")
    name = input()
    fobj_out = open("Texte/"+name + ".txt","w")
	#zeilenanzahl = int(len(Text)/8)
    for i in range(int(len(Text)/32)+1):
        for k in range(4):
            for j in range(8):
                try:
                    fobj_out.write(Text[32*i+8*k+j].upper())
                except IndexError:
                    fobj_out.write(' ') #eigentlich: exit loop
            fobj_out.write(' ')
        fobj_out.write('\n')
    fobj_out.close()
####################################################################################
