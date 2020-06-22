'''
Write a program that maps a list of words into a list of integers representing 
the lengths of the correponding words.

'''
def main():
    m=int(input("size of first list: "))

    listOfWords=[input("Enter the elements of List: ") for i in range(m)]
 
    listOfInts=[len(j) for j in listOfWords]
 
    print ("List of words:",listOfWords)    
    print ("List of wordlength:",listOfInts)


if __name__ == "__main__":
    main()
