'''
The third person singular verb form in English is distinguished by the suffix -s, which is added to 
the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:

If the verb ends in y, remove it and add ies
If the verb ends in o, ch, s, sh, x or z, add es
By default just add s
Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form 
returns its third person singular form. Test your function with words like try, brush, run and fix. 
Note however that the rules must be regarded as heuristic, in the sense that you must not expect 
them to work for all cases. Tip: Check out the string method endswith().

'''
def make_3sg_form(input_verb):
 
    if input_verb.endswith('y'):
        third_person_singular_form=input_verb+'ies'
    elif input_verb.endswith(('o','ch','s','sh','x','z')):
        third_person_singular_form=input_verb+'es'
    else:
        third_person_singular_form=input_verb+'s'
 
    print("Third Person SingularForm of '%s' is '%s'"%(input_verb,third_person_singular_form))

def main(): 
    input_verb=input("Enter the Verb:\n>>")
    make_3sg_form(input_verb)

if __name__ == "__main__":
    main()
