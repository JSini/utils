# import os module
import os

# specify directory name
dirpath = os.path.normpath(input("Enter directory absolute path:\n"))

# specify text to rename your files
text = input("Text for renaming files: ")

#loop over the files to rename
for e, filename in enumerate(os.listdir(dirpath)):
    # old name - full path
    old_name = os.path.join(dirpath, filename)

    # new name - full path
    new_name = os.path.join(dirpath, f"{text}_{e}.jpg")

    # rename file
    os.rename(old_name, new_name)

# print two renamed filenames
print(os.listdir(dirpath)[:2])