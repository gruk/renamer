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
	sort(to_rename)
			
#Rename function
def sort(list_to_rename):
	sorted_list = sorted(list_to_rename)
	if len(sorted_list) == 0:
		print "No files found"
		exit()
	global counter

	#Set current root
	root = re.findall('(^.*\.)[0-9]+\.',list_to_rename[0])[0]
	# print 'setting root as: %s' %root
	# create empty dictionary
	rename_dict = {}
	for item in sorted_list:
		#compare root with current root
		stripped_item = re.findall('(^.*\.)[0-9]+\.',item)[0]
		if stripped_item == root:
			# log.write("%s > " %(item))
			new_name = stripped_item + str(counter) + '.dpx'
			# log.write(new_name + "\n")
			rename_dict[item] = new_name
			# add 1 to the counter
			counter += 1
		#if root is not the same as previous, reset counter to 1001
		else:
			counter = 1001
			root = stripped_item
			# log.write("%s > " %(item))
			# print "file '%s' will be renamed " %(item)
			new_name = stripped_item + str(counter) + '.dpx'
			# print new_name
			# log.write(new_name+ "\n")
			rename_dict[item] = new_name
			# add 1 to the counter
			counter += 1
	checkdict(rename_dict)
	# rename(rename_dict)
	

def checkdict(dictionary_thing):
	#create dictionary
	orig_dict = dictionary_thing
	#create dictionary for dups
	error_dict = {}
	#create list for all values from original dictionary
	values = []
	#create list of keys that need deleting
	to_delete = []
	for key in orig_dict:
		#populate values list
		values.append(orig_dict[key])
	# if the list is not empty, proceed with sorting out the dups
	if len(values) != 0:
		for key in orig_dict:
			#if a key in the original dict matches a value in the list
			if key in values:
				# create a variable with adjusted name
				dup_key = key + '.retry'
				# and add it to the error dictionary
				error_dict[dup_key] = orig_dict[key]
				# add problem key to to_delete list
				to_delete.append(key)
				# rename file
				os.rename(key, dup_key)
		for key in to_delete:
			if key in orig_dict:
				del orig_dict[key]
		#write log files
		for key in error_dict:
			# print "rename from %s to %s" % (key, error_dict[key]) 
			log.write(key+ ' > ' + error_dict[key]+ '\n')
		for key in orig_dict:
			# print "rename from %s to %s" % (key, orig_dict[key])
			log.write(key+ ' > ' + orig_dict[key]+ '\n')
		rename(orig_dict)
		# print error_dict
		rename(error_dict)
	else:
		for key in orig_dict:
			# print "rename from %s to %s" % (key, orig_dict[key])
			log.write(key+ ' > ' + orig_dict[key]+ '\n')
		print 'print working as normal - no dups'
		rename(orig_dict)
	log.close()


def rename(dictionary_thing):
	file_lists = dictionary_thing
	print 'renaming'
	for key in file_lists:
		print 'from :' + key
		print 'to :' + file_lists[key]
		os.rename(key, file_lists[key])
	print 'renaming has been done'
	print 'log file has been written'
	print "%i files updated" % len(file_lists)
	log.close()

if __name__ == '__main__':
	main()


#Helpful regex's:
# \.[0-9]+\.dpx   - collects from the second to last . through to the end of a .dpx file
# (^.*\.)[0-9]+\.  - collects from start of name to second to last '.' inclusive
