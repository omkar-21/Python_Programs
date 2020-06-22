                                                                                                                                                                        '''
Write a function char_freq() that takes a string and builds a frequency listing of the characters 
contained in it. Represent the frequency listing as a Python dictionary. 
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

'''
from collections import Counter

def char_freq(input_string):
 
    dictionary = Counter(input_string)
    return dictionary
         
def main():
    print(char_freq("abbabcbdbabdbdbabababcbcbab"))

if __name__ == "__main__":
    main()
