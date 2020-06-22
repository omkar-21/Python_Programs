"""
Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line
to the screen if it is a palindrome.

"""

import re
import os

def main():
    try:
        with open(input("Enter the file path to read\n>>"),'r') as input_file:            
            lines=input_file.readlines()
            print("Palindromic lines are: ")
            for line in lines:
                pal=re.sub('[^a-zA-Z0-9]','',line).strip()
                if pal==pal[::-1]:
                    print(line)
    except FileNotFoundError:
        print("File or File Path not Found")

if __name__ == "__main__":
    main()

