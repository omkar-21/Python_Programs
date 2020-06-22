
'''
A pangram is a sentence that contains all the letters of the English alphabet at least once, 
for example: The quick brown fox jumps over the lazy dog. 
Your task here is to write a function to check a sentence to see if it is a pangram or not.

'''
import string

def is_pangram(inputed_string):
         
    for i in string.punctuation:
        inputed_string=inputed_string.replace(i,'')
    return not set(string.ascii_lowercase) - set(inputed_string)


 
def main():
    inputed_string = input("Enter the Sentence:\n>>")
    if (is_pangram(inputed_string)):
        print ("Input Sentence is a Pangram")
    else:
        print ("Input Sentence is not a Pangram")

if __name__ == "__main__":
    main()
