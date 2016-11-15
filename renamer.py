#!/usr/bin/env python
# from __future__ import print_function
# from wand.image import Image
# from __future__ import print_function
import os, re
from wand.image import Image


def main():
	print "File renumbererer for Tony"
	print ""
	path = raw_input("enter folder path: ").strip()
	scan(path)

def scan(path):
	results = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if re.search('^\..*', name) == None:
				results.append(os.path.join(root, name))
			else:
				pass


	for item in results:
		# print item
		checkres(item)

def checkres(item):
	with Image(filename=item) as img:
		print item
		print 'width =', img.width
		print 'height =', img.height


if __name__ == '__main__':
	main()



	# def find_all(name, path):
	# # searches for a file in a path and returns a list of the filepaths

	# strippedName = name.strip().split('.')
	# cleanName = strippedName[0]
	# MOVName = cleanName + '.MOV'
	# movName = cleanName + '.mov'
	# mp4Name = cleanName + '.mp4'
	# for root, dirs, files in os.walk(path):
	# 	if MOVName in files:
	# 		clipDict2[MOVName] = clipDict[name]
	# 		searchResult.append(os.path.join(root, MOVName))
	# 		print "%i files found" % count
	# 		count += 1
	# for root, dirs, files in os.walk(path):
	# 	if movName in files:
	# 		clipDict2[movName] = clipDict[name]
	# 		searchResult.append(os.path.join(root, movName))
	# 		print "%i files found" % count
	# 		count += 1
	# for root, dirs, files in os.walk(path):
	# 	if cleanName in files:
	# 		clipDict2[cleanName] = clipDict[name]
	# 		searchResult.append(os.path.join(root, cleanName))
	# 		print "%i files found" % count
	# 		count += 1
	# for root, dirs, files in os.walk(path):
	# 	if mp4Name in files:
	# 		clipDict2[mp4Name] = clipDict[name]
	# 		searchResult.append(os.path.join(root, mp4Name))
	# 		print "%i files found" % count
	# 		count += 1
	# return searchResult


