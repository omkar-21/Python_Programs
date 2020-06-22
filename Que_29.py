"""
Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an
integer n and returns the list of words that are longer than n.
"""


def filter_long_words(words, n):
    return filter(lambda x: len(x) > n, words)

def main():
    m=int(input("Enter size of List:\n>>"))
    words=[input("Enter the words: ") for i in range(m)]
    n=int(input("Enter Integer n:\n>>"))
    print(list(filter_long_words(words,n)))

if __name__ == "__main__":
    main()
