# write a python program that accepts a filename from the user and print the extension of the file

filename=input("file name:")
file_extension=filename.split(".")
print("the extension of the file is :",file_extension[-1])