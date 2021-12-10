# Author RTS 12/9/21

def anagram(w1, w2):
    l1 = list(word1)
    l2 = list(word2)

    s1 = l1.copy()
    s2 = l2.copy()
    s1.sort()
    s2.sort()

    if s1 == s2:
        return("The words " + word1 + ' and ' + word2 + " are anagrams.")
    else:
        return("The words " + word1 + ' and ' + word2 + " are not anagrams.")

word1 = input("Input a word: ")
word2 = input("Input another word: ")
