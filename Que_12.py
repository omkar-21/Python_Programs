'''
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:

****
*********
*******
'''

def histogram(inputList):
 
    for i in inputList:
        print (i*'*')
 
def main(): 
    m=int(input("size of first list: "))
    List=[int(input("Enter a Number: ")) for i in range(m)]
    histogram(List)
    
if __name__=='__main__':
    main()