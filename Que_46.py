"""
An alternade is a word in which its letters, taken alternatively in a strict
sequence, and used in the same order as the original word, make up at least two
other words. All letters must be used, but the smaller words are not
necessarily of the same length.
For example, a word with seven letters where every second letter is used will
produce a four-letter word and a three-letter word.
Here are two examples:
  "board": makes "bad" and "or".
  "waists": makes "wit" and "ass".
Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt,
write a program that goes through each word in the list and tries to make two
smaller words using every second letter. The smaller words must also be members
of the list. Print the words to the screen in the above fashion.
"""

import enchant
from urllib import request


URL = "http://wiki.puzzlers.org/pub/wordlists/unixdict.txt"


def get_words(url):
    words = request.urlopen(url).read().decode("utf-8").split()
    return words

def pairs(w):
    dictionary = enchant.Dict("en_US")
    lenmax = len(w)
    if lenmax < 4:
        return
    word1 = w[::2]
    word2 = w[1::2]

    if dictionary.check(word1) is True & dictionary.check(word2) is True:
        return word1, word2
    return




def alternades(words):
    
    for w in words:
        if pairs(w) is not None:
            word1, word2 = pairs(w)
            print("%s: makes %s and %s"%(w, word1, word2))
    return


def main():
    words = get_words(URL)
    result = [w for w in words if w.isalpha()]
    alternades(result)


if __name__ == "__main__":
    main()