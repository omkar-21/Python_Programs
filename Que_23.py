'''
Define a simple "spelling correction" function correct() that takes a string and sees to it 
that 1) two or more occurrences of the space character is compressed into one, and 
2) inserts an extra space after a period if the period is directly followed by a letter. 
E.g. correct("This   is  very funny  and    cool.Indeed!") should return 
"This is very funny and cool. Indeed!" Tip: Use regular expressions!

'''
import re
 
def correct(input_string):

    new_string = re.sub(r"\s+", " ", input_string)
    
    new_string = new_string.lstrip().rstrip()

    new_string = re.sub(r"\s([.!?,;])", r"\1", new_string)
    new_string = re.sub(r"\.([a-zA-Z])", r". \1", new_string)
    new_string = re.sub(r"\?([a-zA-Z])", r"? \1", new_string)
    print(re.sub(r"\!([a-zA-Z])", r"! \1", new_string))

 
def main(): 
    input_string = "This   is  very funny  and    cool .Indeed !.But      you should.try  this also"
    print(input_string)
    correct(input_string)

if __name__ == "__main__":
    main()
