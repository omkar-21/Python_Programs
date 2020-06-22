'''
In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. 
A simple set of heuristic rules can be given as follows:

If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter before adding ing
By default just add ing
Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form 
returns its present participle form. Test your function with words such as lie, see, move and hug. 
However, you must not expect such simple rules to work for all cases.

'''
def make_ing_form(inputed_word):
    pp_of_inputed_word=""     
    if inputed_word.endswith('e'):
        pp_of_inputed_word = inputed_word[:-1]+'ing'

    elif inputed_word.endswith('ie'):
        pp_of_inputed_word = inputed_word[:-2]+'y'+'ing'
        
    
    elif len(inputed_word)>2:
        if(inputed_word[-3] not in 'aeiou' and inputed_word[-2] in 'aeiou' and inputed_word[-1] not in 'aeiou'):
            pp_of_inputed_word = inputed_word + inputed_word[-1] + 'ing'

    print("Present Participle of word '%s' is '%s'"%(inputed_word,pp_of_inputed_word))

def main():
    make_ing_form('lie')
    make_ing_form('see')
    make_ing_form('move')
    make_ing_form('hug')
                      
if __name__ == "__main__":
    main()
