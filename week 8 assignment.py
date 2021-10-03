import os

filepath = input("enter where you want to save this file:")
if os.path.isdir(filepath):
    print("found the directory")
    fname = input("what do you want to name the file")
    filepath = filepath + "/" + fname + ".txt"
    data = input("enter your name address and phone numbers seperated by commas")
    with open(filepath, 'w') as filehandle:
        filehandle.write(data)
    with open(filepath, 'r') as filehandle:
        fdata = filehandle.read()
    print(fdata)
else:
    print("directory doesn't exist")
