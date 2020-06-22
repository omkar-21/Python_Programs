'''
The function max() from exercise 1) and the function max_of_three() from exercise 
2) will only work for two and three numbers, respectively. 
But suppose we have a much larger number of numbers, or suppose we cannot tell in advance 
how many they are? Write a function max_in_list() that takes a list of numbers and 
returns the largest one.

'''
def max_in_list(number_list):
    if(len(number_list)==0):
        print("List is empty")
        return
    largest=number_list[0]
    for i in range(1,len(number_list)):
        if(largest<number_list[i]):
            largest=number_list[i]
    print("Largest number is:",largest)

def main():
    print("Enter the \'stop\' to end the list")
    number_list=[]
    while(True):
        number=input("Enter the number:\n>>")
        if(number!='stop'):
            number_list.append(float(number))
        else:
            break
        
    max_in_list(number_list)


if __name__ == "__main__":
    main()
