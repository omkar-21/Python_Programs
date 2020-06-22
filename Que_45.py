import os
from os import path
from collections import defaultdict

def search(sequences, min_char, curr_word, current_path,
           current_path_len, longest_path,dic):
 
    current_path[current_path_len] = curr_word
    current_path_len += 1
    if current_path_len == len(longest_path):
        dic[longest_path[0]].append(longest_path[:current_path_len])
        dic[current_path[0]].append(current_path[:current_path_len])
    if current_path_len > len(longest_path):
        longest_path[:] = (current_path[:current_path_len])
        dic.clear()
        dic[longest_path[0]]=[(longest_path)]
    
    last_char_index = ord(curr_word[-1]) - min_char
    if last_char_index >= 0 and last_char_index < len(sequences):
        for pair in sequences[last_char_index]:
            if not pair[1]:
                pair[1] = True
                search(sequences, min_char, pair[0], current_path,
                       current_path_len, longest_path,dic)
                pair[1] = False
 
 
def find_longest_chain(words):
    min_char = ord(min(word[0] for word in words))
    max_char = ord(max(word[0] for word in words))
    sequences = [[] for _ in range(max_char - min_char + 1)]
    for word in words:
        sequences[ord(word[0]) - min_char].append([word, False])
 
    current_path = [None] * len(words)
    longest_path = []
    dic=defaultdict(lambda:[])
    for seq in sequences:
        for pair in seq:
            pair[1] = True
            search(sequences, min_char, pair[0],
                   current_path, 0, longest_path,dic)
            pair[1] = False
 
    return dic 

def main():   
    try:
        with open(input("Enter the file path to read\n>>"),'r') as inputed_file:
            file_to_read=sorted(set(inputed_file.read().rstrip().split(" ")))
            dic = find_longest_chain(file_to_read)
            for i in dic:
                for j in dic[i]:
                    print(j)
    except FileNotFoundError:
        print("File or File Path not Found")

if __name__=='__main__':
    main()