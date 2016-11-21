#Renamer for 2k dpx files

22/11/2016 - renamer.py now prevents renaming files to file names that might already exist.
	Created undo_renamer.py which will reverse the changes made in renamer.py
	undo_renamer.py requires the relevant log file to operate.

(renamer2.py) now relies on names of parent folders for file resolution.
Logs to a file called renamerlog.txt
