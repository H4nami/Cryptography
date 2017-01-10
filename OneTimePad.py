#!/usr/bin/python2
import string
import random


def keygen(lngth,numk):
	alice = open("Alice.txt", "w")
	bob = open("Bob.txt", "w")
	for key in range(0,numk):
		k=''.join(random.choice(string.digits+string.punctuation+string.ascii_letters) for _ in range(lngth)) 
		alice.write(k+"\n")
		bob.write(k+"\n")
	alice.close()
	bob.close()

def cipher(msg,user):
	ciph=""
	if user%2==1:
		file=open("Alice.txt", "r+")
		key=file.readline()
		file.close()
	else:
		file=open("Bob.txt", "r+")
		key=file.readline()
		file.close()

	count=0
	for lttr in msg:
		ciph+=chr(ord(lttr)^ord(key[count%len(key)]))
		count+=1

	return ciph


	
def inicio():
	print "You need to generate the one time pads"
	lenk=int(raw_input("Introduce the length of the keys: "))
	numk=int(raw_input("Introduce the number of keys: "))
	keygen(lenk,numk)
	
	
	cont=0
	usr=["Alice", "Bob"]
	while True:
		if cont==numk:
			print "\n"+str(cont)+" "+usr[0]+" Says:\n"+"Ciphertext: "+ciphMsg+"\n"+"Plain text: "+plnMsg
			print "\n\n\n##### You need to generate more keys #####\n\n\n"
			break


		if cont%2==1:
			print "\n"+str(cont)+" "+usr[0]+" Says:\n"+"Ciphertext: "+ciphMsg+"\n"+"Plain text: "+plnMsg
			mssge=raw_input("\nWrite a message or type exit\n")

			ciphMsg=cipher(mssge,cont)
			file=open("Bob.txt","r")
			lines=file.readlines()
			file.close()
			del lines[0]
			file=open("Bob.txt","w+")
			file.writelines(lines)
			file.close()

			plnMsg=cipher(ciphMsg,cont)
			cont+=1
			file=open("Alice.txt","r")
			lines=file.readlines()
			file.close()
			del lines[0]
			file=open("Alice.txt","w+")
			file.writelines(lines)
			file.close()

		else:
			if cont==0:
				mssge=raw_input("Write a message or type exit\n")
			else:
				print "\n"+str(cont)+" "+usr[1]+" Says:\n"+"Ciphertext: "+ciphMsg+"\n"+"Plain text: "+plnMsg
				mssge=raw_input("\nWrite a message or type exit\n")
			ciphMsg=cipher(mssge,cont)
			file=open("Alice.txt","r")
			lines=file.readlines()
			file.close()
			del lines[0]
			file=open("Alice.txt","w+")
			file.writelines(lines)
			file.close()

			plnMsg=cipher(ciphMsg,cont)
			cont+=1
			file=open("Bob.txt","r")
			lines=file.readlines()
			file.close()
			del lines[0]
			file=open("Bob.txt","w+")
			file.writelines(lines)
			file.close()



		if mssge.lower()=="exit":
			break
inicio()







