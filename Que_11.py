'''
Define a function generate_n_chars() that takes an integer n and a character c and 
returns a string, n characters long, consisting only of c:s. 
For example, generate_n_chars(5,"x") should return the string "xxxxx". 
(Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". 
For the sake of the exercise you should ignore that the problem can be solved in this manner.)

'''
def generate_n_chars(input_number, input_char):
    output_string=""
     
    for i in range(input_number):
        output_string+=input_char
 
    return output_string
def main():       
    while(True):
        try:
            input_char = input("Enter the Character:\n>>")
            if len(input_char)>1:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print("ERROR : Input a Character, String of size 1.")
        
    input_number = int(input("Enter the number of times \'" +str(input_char) +"\' to be printed: ")) 
    print("The generated string is:",generate_n_chars(input_number,input_char))

if __name__ == "__main__":
    main()
