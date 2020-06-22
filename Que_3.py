'''
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, 
but writing it yourself is nevertheless a good exercise.)

'''

def findLen(str1): 
    counter = 0    
    for i in str1: 
        counter += 1
    print("Length of string is",counter) 
  
def main():
    str1=input("Enter the string: ")
    findLen(str1)

if __name__=='__main__':
    main()