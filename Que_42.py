"""
A sentence splitter is a program capable of splitting a text into sentences.
The standard set of heuristics for sentence splitting includes
(but isn't limited to) the following rules:
Sentence boundaries occur at one of "." (periods), "?" or "!", except that
a. Periods followed by whitespace followed by a lower case letter are not
sentence boundaries.
b. Periods followed by a digit with no intervening whitespace are not
sentence boundaries.
c. Periods followed by whitespace and then an upper case letter, but preceded
by any of a short list of titles are not sentence boundaries. Sample titles
include Mr., Mrs., Dr., and so on.
d. Periods internal to a sequence of letters with no adjacent whitespace are
not sentence boundaries (for example, www.aptex.com, or e.g).
e. Periods followed by certain kinds of punctuation (notably comma and more
periods) are probably not sentence boundaries.
Your task here is to write a program that given the name of a text file is
able to write its content with each sentence on a separate line.
Test your program with the following short text:
Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for
it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't
true... Well, with a probability of .9 it isn't.
The result should be:
Mr. Smith bought cheapsite.com for 1.5 million dollars,\
 i.e. he paid a lot for it.
Did he mind?
Adam Jones Jr. thinks he didn't.
In any case, this isn't true...
Well, with a probability of .9 it isn't.
"""

import os
import re


def text_splitter(splitted_text,result):
    
    
    splitted_text = re.sub(r"(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])", r".\n\1", splitted_text)
    splitted_text = re.sub(r"\?\s", r"?\n", splitted_text)
    splitted_text = re.sub(r"!\s", r"!\n", splitted_text)

    result.write(splitted_text)
    print("Splitted Text File is in your current directory.\nName of file is splitted_text.txt")


def main():
    try:
        with open(input("Enter the file path to read\n>>"),'r') as inputed_file, open("splitted_text.txt","w+") as output_file:
            splitted_text=inputed_file.read().lstrip().rstrip()    
            text_splitter(splitted_text,output_file)
    except FileNotFoundError:
        print("File or File Path not Found")


if __name__ == "__main__":
    main()
