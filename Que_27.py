"""
Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.
Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list
comprehensions.

"""

def lengths_using_loop(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def lengths_using_map(words):
    return map(len, words)

def lengths_using_list_comp(words):
    return [len(word) for word in words]

def main():
    m=int(input("Enter the size of List:\n>>"))
    words=[input("Enter the word: ") for i in range(m)]
    print("List Using Loop:",lengths_using_loop(words))

    print("List Using Map:",list(lengths_using_map(words)))

    print("List Using List Comperihension:",lengths_using_list_comp(words))

if __name__ == "__main__":
    main()
