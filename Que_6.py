'''
Define a function sum() and a function multiply() that sums and multiplies 
(respectively) all the numbers in a list of numbers. 
For example, sum([1, 2, 3, 4]) should return 10, 
and multiply([1, 2, 3, 4]) should return 24.

'''
import functools

def addListElements(inputed_list):
    return functools.reduce(lambda a,b:a+b,inputed_list)     
 
 
def multiplyListElements(inputed_list):
   return functools.reduce(lambda a,b:a*b,inputed_list)

def main():
    m=int(input("size of first List: "))
    inputed_list=[float(input("Enter the number: ")) for i in range(m)] 
    print("The initial list is:",inputed_list )
    print("Sum of the elements of the list is:",addListElements(inputed_list ))
    print("Multiplied value of the elements of the list is:",multiplyListElements(inputed_list ))

if __name__ == "__main__":
    main()
 
