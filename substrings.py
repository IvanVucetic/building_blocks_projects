from collections import Counter

dictionary = ["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"]

def substrings(word, dictionary):
    '''Checks substrings of a string for occurence in dictionary.'''

    word_apart = []
    for i in range(0,len(word)):
        for j in range(i,len(word)+1):
            if word[i:j] != "" and word[i:j] in dictionary:
                word_apart.append(word[i:j])
            else:
                pass

    print word_apart
    print Counter(word_apart)

substrings("Howdy partner, sit down! How's it going?", dictionary)