'''
Write a function find_longest_word() that takes a list of words and returns the length of the 
longest one. Use only higher order functions.

'''

def find_longest_word(words):
    return max(map(len, words))

def main():
    m=int(input("Enter size of List:\n>>"))
    words=[input("Enter the words: ") for i in range(m)]
    print("Length of Longest Word:",find_longest_word(words))

if __name__ == "__main__":
    main()
