'''
Write a function translate() that will translate a text into "rövarspråket" 
(Swedish for "robber's language"). That is, double every consonant and place an 
occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".

'''

def vowelChecker (character):  
    if character in ['a','e','i','o','u','A','E','I','O','U']:
        return True
    return False
    
def translator(stringToTranslate):
    translatedString = ""
 
    for i in stringToTranslate:
        if (not vowelChecker(i) or i == " "):
            translatedString = translatedString+i
        elif vowelChecker(i):
            translatedString = translatedString+i+'o'+i
 
    return translatedString
 
def main():
    stringToTranslate = input("Enter the string to translate: ");
    print("The translated string is:",translator(stringToTranslate))
 
if __name__ == "__main__":
    main()
