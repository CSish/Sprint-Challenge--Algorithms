'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):

    #non recursive preliminary test
    # count = word.count('th')
    
    # for i in range(len(word) - 1): 
    #     if word[i] == 't' and word[i+1] == 'h':
    #         count +=1
    # return count
    
    if word =='th' or 'th' not in word:
        return count
    # if word.index('th'):
    #     # print(word.index('th'))
    #     i = word.index('th')
    #     # print(i)
    #     new_str = word[i: i+2]
    #     print(new_str)
    
    word = word.replace('th', ' ', 1)
    print(word)
    count += 1


    return count_th(word, count)
