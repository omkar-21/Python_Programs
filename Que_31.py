'''
Implement the higher order functions map(), filter() and reduce(). 
(They are built-in but writing them yourself may be a good exercise.)

'''
#solved as per Que27
def implement_map(words):
    List=[len(word) for word in words]
    return List

#solved as per Que29
def implement_filter(words,n):
    List=[word  for word in words  if len(word)>n]
    return List

##solved as per Que26
def implement_reduce(number,n):
    largest=number[0]
    if(len(number)>1):
        for i in range(1,n):
            if(largest<number[i]):
                largest=number[i]
    return largest
def main(): 
    m=int(input("Enter size of List:\n>>"))
    words=[input("Enter the words: ") for i in range(m)]
    print("myMap function answer which returns length of each word:",implement_map(words))
    n=int(input("Enter the lenght for filter function\n>>"))
    print("myFilter function answer which returns list of words whose length greater than n:",implement_filter(words,n))
    size=int(input("Enter size n of Integer List for Reduce funtion:\n>>"))
    number=[float(input("Enter the Integer: ")) for i in range(size)]
    print("myReduce fucntion which return Largest number among numbers: ",implement_reduce(number, size))

if __name__ == "__main__":
    main()
