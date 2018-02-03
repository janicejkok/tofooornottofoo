
def answer(s):
    num = 0      # num is used to track the number of repeated strings with same sequence
    newlen, prevlen = len(s)//2, len(s)
    split = list(s)
    if len(set(s)) ==1: #if the string contains all the same letters, return the number of letters
        return len(s)
    if len(s)%2==1: #if the string is odd number, the "no leftover" rule is not satisfied. 
        return 1  #so it would just be one unique pie.
    if split[0:newlen] != split [newlen:prevlen]: #to check if the string is a unique string w/0 repeated sequences
        return 1
    for i in s: 
        if split[0:newlen] == split [newlen:prevlen]: # to check if the first half of the string is identical to the second half
            num +=2   #update num if there are identical strings.
            prevlen, newlen = newlen, newlen//2 #this will break the half of the string into two halves
    return num 
