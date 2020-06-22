'''
Define a function overlapping() that takes two lists and returns True 
if they have at least one member in common, False otherwise. 
You may use your is_member() function, or the in operator, 
but for the sake of the exercise, you should (also) write it using two nested for-loops.

'''

def common_data(List1, List2): 
    for x in List1: 
        for y in List2: 
            if x == y: 
                print(True)
                return   
    print(False) 

def main():
    m=int(input("size of first array: "))
    n=int(input("size of first array: "))
    List1=[input("Enter the item for 1st List: ") for i in range(m)]
    List2=[input("Enter the item for 2nd List: ") for i in range(n)]
    common_data(List1,List2)

if __name__ == "__main__":
    main()
