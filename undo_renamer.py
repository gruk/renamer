#!/usr/bin/env python

#IMPORTING MODULES
import sys, os

def main():
	if len(sys.argv) < 2:
		#Collect Path
		logfile = raw_input("enter logfile path: ").strip()
		#Scan Path
		prep(logfile)
	else:
		logfile = sys.argv[1]
		prep(logfile)

def prep(logfile):
	#create dictionary
	file_lists = {}
	log = open(logfile, 'r')
	for line in log:
		linecut = line[:-1]
		splitline = linecut.split(' > ')
		file_lists[splitline[0]] = splitline[1]
	log.close()
	rename(file_lists)

def rename(dictionary_thing):
	file_lists = dictionary_thing
	retry_dict = {}
	print 'renaming'
	for key in file_lists:
		print 'from ' + file_lists[key]
		print 'to ' + key
		os.rename(file_lists[key], key)
	#Sort out the .retry files
	for key in file_lists:
		if key[-6:] == '.retry':
			var_key = key[:-6]
			retry_dict[var_key] = key
			for key in retry_dict:
				os.rename(retry_dict[key], key)
	print 'renaming has been undone'
	print '%s files updated (%i files renamed twice)' %(len(file_lists) + len(retry_dict), len(retry_dict))

if __name__ == '__main__':
	main()
