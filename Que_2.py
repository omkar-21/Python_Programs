'''
Define a function max_of_three() that takes 
three numbers as arguments and returns the largest of them.

'''

def max_of_three(num1, num2, num3): 
  
    if (num1 >= num2) and (num1 >= num3): 
        largest = num1 
  
    elif (num2 >= num1) and (num2 >= num3): 
        largest = num2 
    else: 
        largest = num3 
          
    print("Largest number among is:",largest) 

def main():
    num1, num2, num3 = (float(input("Enter Your Number: ")) for i in range(3))
    max_of_three(num1, num2, num3)


if __name__ == "__main__":
    main()
