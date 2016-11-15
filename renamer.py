#!/usr/bin/env python

#IMPORTING MODULES
import os, re
from wand.image import Image

#DEFINE GLOBAL VARIABLE
counter = 1000

def main():
	#INTRO
	print "File renumbererer for Tony"
	print ""
	#Collect Path
	path = raw_input("enter folder path: ").strip()
	#Scan Path
	scan(path)

def scan(path):
	#Create list

	#Look through Directory
	for root, dirs, files in os.walk(path):
		#Loop through all files
		for name in files:
			#If file is hidden - ignore it. Otherwise send it to checker
			if re.search('^\..*', name) == None:
				# pass both path+name and filename to checker
				check(os.path.join(root, name), name, root)
			else:
				pass


#Check Resolution of files
def check(item,name, path):
	#If file size is less than 15MB
	if os.stat(item).st_size <= 15000000:
		#Use ImageMagick to check the dimensions of the image
		with Image(filename=item) as img:
			#If image width is less than 2200 pixels - send it to the renaming function
			if img.width <= 2200:
				#pass path+name and name to renamer
				rename(item, name, path)
			#Otherwise print error
			else:
				print "ERROR: File '%s' has a width greater than 2200 pixels" %item
	#Otherwise print error
	else:
		print "ERROR: file '%s' is larger than 15MB" %item

#Rename function
def rename(item, name, path):
	global counter
	# add 1 to the counter
	counter += 1
	#Prove that data gets here
	print "file '%s' at path '%s' will be renamed to: " %(name, item)
	#set name variable
	init_name = name
	#remove current numbers from the name
	split_name = init_name.split('.',1)[0]
	#add new number to the name and add .dpx
	new_name = split_name + '.' + str(counter) + '.dpx'
	#print finalised name
	new_full_name = path + '/' + new_name
	os.rename(item, new_full_name)

if __name__ == '__main__':
	main()

