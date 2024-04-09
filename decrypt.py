#decryption program
import os
from cryptography.fernet import Fernet 

#to find all the files in the directory to attack
files = []
for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py" : #to exclude these necessary files from being encrypted
		continue
	if os.path.isfile(file): #to make sure folder is not encrypted only files
		files.append(file)

#get the key for decryption from thekey.key
with open("thekey.key","rb") as key:
	secret_key = key.read()

#looping over the files for decryption
for file in files:
	with open(file,"rb") as thefile: #reading content
		contents = thefile.read()

	decrypted_content = Fernet(secret_key).decrypt(contents) #content decryption

	with open(file,"wb") as thefile:
		thefile.write(decrypted_content) #writing content
