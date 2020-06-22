'''
Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I".

'''
def main():
    str1=list(input("Enter the string: "))
    for i,j in zip(range(len(str1)//2),range((len(str1)-1),(len(str1)-1)//2,-1)):
        str1[i],str1[j]=str1[j],str1[i]
    # or we can use str1[::-1]
    print("Reversed string : "+"".join(i for i in str1))

if __name__ == "__main__":
    main()
