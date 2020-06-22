"""
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a 
new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. 
Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the 
sets of words that share the same characters that contain the most words in them.
"""


from collections import defaultdict
from urllib import request

URL = "http://wiki.puzzlers.org/pub/wordlists/unixdict.txt"

def get_words(url):
    words = request.urlopen(url).read().decode("utf-8").split()
    return words 
    
def map_words(words):
    group_words = defaultdict(list)
    
    for word in words:
        group_words["".join(sorted(word))].append(word)
    return group_words

def main():
    words = get_words(URL)
    group_words=map_words(words)
    userWord=input("Enter the word to find anagram of that word in the given Text\n>>")
    if userWord in group_words:
        print("Anagrams Present in Given Text are:",group_words["".join(sorted(userWord))])
    else:
        print("No Words")

if __name__ == "__main__":
    main()
