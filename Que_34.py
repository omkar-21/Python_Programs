"""
Write a procedure char_freq_table() that, when run in a terminal, accepts a
file name from the user, builds a frequency listing of the characters
contained in the file, and prints a sorted and nicely formatted character
frequency table to the screen.
"""


from collections import Counter
import os

def main():
    try:
        with open(input("Enter the file path to read\n>>"),'r') as input_file:
            dic=Counter(input_file.read())
            print("Count of Character using Inbuilt Function:",sorted(dic.items()))
    except FileNotFoundError:
        print("File or File Path not Found")

if __name__ == "__main__":
    main()
