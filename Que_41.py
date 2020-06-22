"""
In a game of Lingo, there is a hidden word, five characters long. The object of
the game is to find this word by guessing, and in return receive two kinds of
clues:
1) the characters that are fully correct, with respect to identity as well as
to position,
and
2) the characters that are indeed present in the word, but which are placed in
the wrong position.
Write a program with which one can play Lingo.
Use square brackets to mark characters correct in the sense of 1),
and ordinary parentheses to mark characters correct in the sense of 2).
Assuming, for example, that the program conceals the word "tiger",
you should be able to interact with it in the following way:
>>> import lingo
snake
Clue: snak(e)
fiest
Clue: f[i](e)s(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]
"""

import os
import random
import re

def lingo(random_word):
    list1=[]
    list3=[]
    while True:

        user_word = input("Guess the Word\n>>")

        if user_word == random_word:
            return

        if len(user_word) != len(random_word):
            print("Your guess must be %d letters long."%(len(random_word)))
            user_word = input("Guess the Word\n>>")
            continue
        
        guess=""
        list1=[i for i in range(len(random_word)) if(random_word[i]==user_word[i])]
        list3=[j for i in set(range(len(random_word)))-set(list1) if(random_word[i] in user_word and i not in list1) for j in range(len(random_word)) if(user_word[j]==random_word[i] and j not in list3 and j not in list1)]
        guess="".join(['['+user_word[i]+']' if i in list1 else '('+user_word[i]+')' if i in list3 else user_word[i] for i in range(len(random_word))])
        print("Clue: %s"%(guess))

def main():
    try:
        with open(input("Enter the file path to read\n>>"),'r') as inputed_file: 
            file_to_read=inputed_file.readlines()
            words=[word for line in file_to_read for word in re.sub('[^\w\s]','',line).strip().split(" ")]
            random_word = random.choice(words)
            lingo(random_word)
    except FileNotFoundError:
        print("File or File Path not Found")

if __name__ == "__main__":
    main()
