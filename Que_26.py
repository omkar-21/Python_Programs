'''
Using the higher order function reduce(), write a function max_in_list() that takes a list of 
numbers and returns the largest one. Then ask yourself: why define and 
call a new function, when I can just as well call the reduce() function directly?

'''
import functools

def max_in_list(list_of_numbers):
    return functools.reduce(lambda x,y: x if x>y else y,list_of_numbers)

def main():
    m=int(input("Enter size of List:\n>>"))
    list_of_numbers=[float(input("Enter the number: ")) for i in range(m)]
    print("Maximum Number in List:",max_in_list(list_of_numbers))

if __name__ == "__main__":
    main()
