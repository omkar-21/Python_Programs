'''
Represent a small bilingual lexicon as a Python dictionary in the following fashion 
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and 
use it to translate your Christmas cards from English into Swedish. 
That is, write a function translate() that takes a list of English words and returns a list of 
Swedish words.

'''

def translate(inputString):

    dictionary = {"merry":"god",
              "christmas":"jul",
              "and":"och",
              "happy":"gott",
              "new":"nytt",
              "year":"år"}

    translatedString = [dictionary[i] for i in inputString.split(" ") if i in dictionary]

    return (translatedString)
             
def main():
    inputString = "merry christmas and happy new year"
 
    if (translate(inputString)) == "":
        print("The sentence can not be translated")
    else:
        print(" ".join(translate(inputString)))

if __name__ == "__main__":
    main()
