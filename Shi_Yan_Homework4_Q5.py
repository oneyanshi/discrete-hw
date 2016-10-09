'''
PYTHON VERSION 2.7.10
AUTHOR: YAN SHI
UPDATED: October 9, 2016

PROMPT:
    Write a program which prints out all rearrangements of a word, with no repeats.
    Assume that a word consists of capital English letters

    Example:

    ABC
    Permutations:
    ABC
    ACB
    BAC
    BCA
    CAB
    CBA

'''
def permutation(word):
    letter = [word[0]] #first letter into the list!
    for i in range(1, len(word)): #traversing through the word
        return_list = [] #create the return list
        for item in letter:
            return_list.append(item+word[i])
            for j in range(len(item)):
                return_list.append(item[0:j] + word[i] + item[j:])
        letter = return_list
    return return_list

word = raw_input("Input a word that you'd like to see the permutations of: ").lower()
print permutation(word)
