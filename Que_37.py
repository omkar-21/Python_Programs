"""
Write a program that given a text file will create a new text file in which all
the lines from the original file are numbered from 1 to n (where n is the
number of lines in the file).
"""

import os

def number_lines(file_path, path_for_new_file):
    try:    
        with open(file_path,'r') as input_file, open(path_for_new_file,"w+") as output_file:
            lines=input_file.readlines()
            for no,line in enumerate(lines,1):
                output_file.write("%d) %s" %(no,line) )
            return
    except FileNotFoundError:
        print("File or File Path not Found")

def main():
    file_path=input("Enter the file path:\n>> ")
    path_for_new_file=input("Enter the File Path with File Name for New File:\n>> ")
    number_lines(file_path,path_for_new_file)


if __name__ == "__main__":
    main()
    


