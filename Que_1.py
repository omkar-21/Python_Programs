'''
Define a function max() that takes two numbers as arguments and returns the largest of them. 
Use the if-then-else construct available in Python. 
(It is true that Python has the max() function built in, 
but writing it yourself is nevertheless a good exercise.)

'''
def maximum(num1,num2): 
  
    if (num1 >=num2): 
        print("largest Number is: ",num1) 
    
    else:
        print("largest Number is: ",num2)

def main():
    num1=float(input("Enter Your First Number  : "))
    num2=float(input("Enter Your Second Number : "))
    maximum(num1,num2) 

if __name__=='__main__':
    main()