'''
Define a function is_palindrome() that recognizes palindromes 
(i.e. words that look the same written backwards). 
For example, is_palindrome("radar") should return True.

'''
'''
Que 8. palindrome.
alternative: return s==s[::-1] # using string slice
'''

def palindrome(str1):
    if str1==str1[::-1]:
        print("palindromic String")
    else:
        print("Not Palindromic String")

def main():
    str1=input("Enter Your String: ")
    palindrome(str1.lower())    

if __name__ == "__main__":
    main()
