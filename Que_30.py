"""
Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"} and use it to translate your
Christmas cards from English into Swedish. Use the higher order function map() to write a function translate() that
takes a list of English words and returns a list of Swedish words.
"""


def translate(words):
    lexicon = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
    words=words.split(" ")
    return map(lambda word:lexicon[word] if word in lexicon else "word not found", words)
def main():
    words=input("Enter Text to Translate to Swedish:\n>>")
    print(list(translate(words)))

if __name__ == "__main__":
    main()
