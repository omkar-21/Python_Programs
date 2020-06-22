'''
Write a function filter_long_words() that takes a list of words and an integer n and 
returns the list of words that are longer than n.

'''

def filter_long_words(inputList,inputInteger):

    listOfWords=filter(lambda i:len(i)>inputInteger,inputList)
    return list(listOfWords)

def main(): 
    m=int(input("size of first list: "))
    input_list_of_words = [input("Enter the string: ") for i in range(m)] 
    input_word_length = int(input("Enter the length: "))
    print ("String which are grater than given input integer:",filter_long_words(input_list_of_words,input_word_length))

if __name__ == "__main__":
    main()