'''
Write a function that takes a character (i.e. a string of length 1) and 
returns True if it is a vowel, False otherwise.

'''

def vowel_or_consonant(character): 
    if character in ['a','e','i','o','u','A','E','I','O','U']:
        print("True") 
    else: 
        print("False")

  
def main():

    while(True):
        try:
            character = input("Enter the Character:\n>>")
            if len(character)>1:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print("ERROR : Input a Character, String of size 1.")
        
        #or we can use getch() module to accept character as input
    
    vowel_or_consonant(character)

if __name__ == "__main__":
    main()
