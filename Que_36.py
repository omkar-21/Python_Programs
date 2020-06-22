"""
A hapax legomenon (often abbreviated to hapax) is a word which occurs only
once in either the written record of a language, the works of an author,
or in a single text. Define a function that given the file name of a text
will return all its hapaxes. Make sure your program ignores capitalization.
"""


import os
import re

def hapax(file_path):
    try:
        with open(file_path,'r') as inputed_file:
            file_to_read=inputed_file.readlines()
            words=[word for line in file_to_read for word in re.sub('[^\w\s]','',line).strip().split(" ")]
            result = filter(lambda word: words.count(word) == 1, words)
            print(list(result))
            return
    except FileNotFoundError:
        print("File or File Path not Found")

def main():
    file_path=input("Enter the file path:\n>> ")
    hapax(file_path)


if __name__ == "__main__":
    main()
