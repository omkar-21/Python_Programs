'''
Write a function find_longest_word() that takes a list of words and 
returns the length of the longest one.

'''
def find_longest_word(word):
    res = [len(ele) for ele in word] 
    return word[res.index(max(res))]

def main():
    m=int(input("size of first list\n>>"))
    inputed_word = [input("Enter the word\n>>") for i in range(m)]  
    print("The original list :",inputed_word) 
    print("Longest Word is: ",find_longest_word(inputed_word))

if __name__ == "__main__":
    main()
