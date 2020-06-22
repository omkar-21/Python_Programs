"""
Write a program that will calculate the average word length of a text stored in
a file (i.e the sum of all the lengths of the word tokens in the text, divided
by the number of word tokens).
"""

import os
import re

def average_len(file_path):
    try:

        with open(file_path,'r') as input_file:

            file_to_read=input_file.readlines()
            words=[word for line in file_to_read for word in re.sub('[^\w\s]','',line).strip().split(" ")]
            word = list(map(len, words))
            average_length = int(sum(word) / len(word))
            return average_length

    except FileNotFoundError:
        print("File or File Path not Found")


def main():
    file_path=input("Enter the file path:\n>> ")
    print("Average Length:",average_len(file_path))


if __name__ == "__main__":
    main()
