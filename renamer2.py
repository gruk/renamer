#!/usr/bin/env python

#IMPORTING MODULES
import os, re, sys
from time import localtime, strftime
#DEFINE GLOBAL VARIABLE
counter = 1001

#CREATE AND OPEN LOG FILE WITH CURRENT TIME AND DATE ATTACHED
current_time = strftime("%Y%m%d%H%M", localtime())
os.system("touch renamerlog%s.txt" % current_time)
log = open("renamerlog%s.txt" % current_time, 'w')


def main():
	#INTRO
	print "File renumbererer"
	print "Designed for use with GTS_2KDRAMA files"
	print "Will rename .dpx files which are nested inside 2k resolution folders provided they are larger than 15MB"
	print ""
	if len(sys.argv) < 2:
		#Collect Path
		path = raw_input("enter folder path: ").strip()
		#Scan Path
		scan(path)
	else:
		path = sys.argv[1]
		scan(path)



def scan(path):
	#Create list
	to_rename = []
	#Look through Directory
	for root, dirs, files in os.walk(path):
		#Loop through all files
		for name in files:
			#Check to see if resolution folder starts with a '2'
			if re.search('2[0-9+]{3}[x][0-9+]{4}', root) == None:
				pass
			else:
				#If file is hidden - ignore it. Otherwise send it to renamer
				if re.search('^\..*', name) == None:
					#If file size is less than 15MB
					if os.stat(os.path.join(root, name)).st_size <= 15000000:
						#If file is a .dpx then send to renamer
						if name[-4:] == ".dpx":
							# pass both path+name and filename to renamer
							to_rename.append(os.path.join(root, name))
						else:
							pass
					else:
						pass
				else:
					pass
	rename(to_rename)
			
#Rename function
def rename(list_to_rename):
	sorted_list = sorted(list_to_rename)
	global counter

	#Set current root
	root = re.findall('^.*PLATE\.',list_to_rename[0])[0]
	# print 'setting root as: %s' %root

	for item in sorted_list:
		#compare root with current root
		stripped_item = re.findall('^.*PLATE\.',item)[0]
		if stripped_item == root:
			log.write("%s > " %(item))
			new_name = stripped_item + str(counter) + '.dpx'
			log.write(new_name + "\n")
			os.rename(item, new_name)
			# add 1 to the counter
			counter += 1
		#if root is not the same as previous, reset counter to 1001
		else:
			counter = 1001
			root = stripped_item
			log.write("%s > " %(item))
			# print "file '%s' will be renamed " %(item)
			new_name = stripped_item + str(counter) + '.dpx'
			# print new_name
			log.write(new_name+ "\n")
			os.rename(item, new_name)
			# add 1 to the counter
			counter += 1
	print "Job Done"
	print "%i files updated" % len(sorted_list)
	log.close()

if __name__ == '__main__':
	main()


