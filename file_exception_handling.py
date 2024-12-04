# -*- coding: utf-8 -*-
#This line tells the interpreter to use UTF-8 encoding, preventing an encoding error.

#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read
try:
    #ask user for filename
    filename = input("Enter the filename: ")

    #attempt to open and read the file
    with open(filename, "r") as file:
        data = file.read()
        print("File content: ")
        print(data)
except FileNotFoundError:
    print("File not found. Please check the file name")
except Exception as e:
    print("An error occured: .format{e}")
finally:
    #only closes the file if successfully opened
    try:
        file.close()
    except NameError:
        pass