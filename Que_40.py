"""
An anagram is a type of word play, the result of rearranging the letters of a
word or phrase to produce a new word or phrase, using all the original letters
exactly once;
e.g., orchestra = carthorse, A decimal point = I'm a dot in place.
Write a Python program that, when started
1) randomly picks a word w from given list of words,
2) randomly permutes w (thus creating an anagram of w),
3) presents the anagram to the user,
and
4) enters an interactive loop in which the user is invited to guess the
original word.
It may be a good idea to work with (say) colour words only.
The interaction with the program may look like so:
>>> import anagram
Colour word anagram: onwbr
Guess the colour word!
black
Guess the colour word!
brown
Correct!
"""
import re
import random
import os


def open_file(file_path):    

    if(path.isfile(file_path)):
        file_to_read=open(file_path,'r')
        return file_to_read
    else:
        print("file not exit")
        exit(1)


def anagram(file_to_read):
    
    words=[word for line in file_to_read for word in re.sub('[^\w\s]','',line).strip().split(" ")]
    random_word = random.choice(words)
    permutted_word = ''.join(random.sample(random_word, len(random_word)))
    print("Colour word anagram: %s" %(permutted_word))
    user_word = input("Guess the colour word!\n>>").lower()

    while user_word != random_word.lower():
        user_word = input("Guess the colour word!\n>>").lower()

    print("Correct!")
    return

def main():
    try:
        with open(input("Enter the file path to read\n>>"),'r') as inputed_file:
            anagram(inputed_file.readlines())

    except FileNotFoundError:
        print("File or File Path not Found")

if __name__ == "__main__":
    main()