from sys import argv
import random
import string


def keygen(NumKeys):
	Keys=open('Keys.txt','w+')
	Fl2Send=open('Fl2Send.txt','w+')
	cont=1
	for key in range(0,int(NumKeys)):
		k=''.join(random.choice(string.digits+string.punctuation+string.ascii_letters) for _ in range(100)) 
		Keys.write(str(cont)+' ### '+k+'\n')
		Fl2Send.write(rot13(str(cont))+' ### '+rot13(k)+'\n')
		print rot13(str(cont))+' ### '+rot13(k)+'\n'
		cont+=1
	Keys.close()
	Fl2Send.close()


def rot13(msg):
	alph=map(chr, range(32,256))
	mod=len(alph)
	ciph=""
	for lttr in msg:
			ciph+=alph[(alph.index(lttr)+13)%mod]
	return ciph


keygen(argv[1])