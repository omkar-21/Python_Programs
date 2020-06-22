'''
Write a function is_member() that takes a value (i.e. a number, string, etc) x 
and a list of values a, and returns True if x is a member of a, False otherwise. 
(Note that this is exactly what the in operator does, 
but for the sake of the exercise you should pretend Python did not have this operator.)

'''
def is_member(item_to_check, inputed_list):
    if(item_to_check in inputed_list):
        print("True")
    else:
        print("False")    

def main():
    m=int(input("size of first list: "))
    inputed_list=[input("Enter List item: ") for i in range(m)]
    item_to_check = input("Enter the item to check in the printed list: ")
    is_member(item_to_check,inputed_list)


if __name__ == "__main__":
    main()
