'''
Write a version of a palindrome recognizer that also accepts phrase palindromes such as 
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", 
"Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir", or 
the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are 
usually ignored.

'''
import string

def palindrome(inputed_string):
    for i in string.punctuation:
        inputed_string=inputed_string.replace(i,'')
    return inputed_string==inputed_string[::-1]

def main():
    inputed_string=input("input phrases: ")
    print(palindrome(inputed_string.replace(" ",'').lower()))

if __name__ == "__main__":
    main()
