"""
Your task in this exercise is as follows:
Generate a string with N opening brackets ("[") and N closing brackets ("]"),
in some arbitrary order.
Determine whether the generated string is balanced; that is,
whether it consists entirely of pairs of opening/closing brackets
(in that order), none of which mis-nest.
Examples:
   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
"""



def are_parantheses_balanced(expr) : 
    
    if expr.startswith("]") and expr.endswith("["):
        return False
    if expr=="":
        print("Empty String Found")
        return False
    else:
        balance = 0
        for char in expr:
            if balance >= 0:
                if char == "[":
                    balance += 1
                elif char == "]":
                    balance -= 1
                else:
                    print("Found paranthesis other than '[' & ']'")
                    return False
    if balance == 0:
        return True
    return False

def main():
    expr=input("Enter the expression contains '[' &']' to check whether it's Balanced or Not\n>>")  
    if are_parantheses_balanced(expr) : 
        print("Balanced");  
    else : 
        print("Not Balanced");  
  

if __name__ == "__main__" :  
    main()