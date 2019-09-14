'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    #searches for 'th' in the word
    i = word.find("th")
    #if not found return 0
    if i == -1:
        return 0
    #finds the first instance of 'th' at index i. We call the function again
    #starting from i + 2. 2 being the length of 'th'
    return 1 + count_th(word[i+2:])