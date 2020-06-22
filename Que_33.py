'''
According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase 
backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that 
accepts a file name (pointing to a list of words) from the user and finds and prints all pairs of words 
that are semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the word list, 
the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!

'''
import os

def main():
    try:
        with open(input("Enter the file path to read\n>>"),'r') as input_file:            
            lines=input_file.readlines()
            words=[word for line in lines for word in line.strip().split(" ")]
            seen = set()
            for word in words:
                if word not in seen:
                    if word[::-1] in seen:
                        print(word, word[::-1])
                seen.add(word)

    except FileNotFoundError:
        print("File or File Path not Found")


if __name__ == "__main__":
    main()
