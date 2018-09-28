import nltk
from nltk.corpus import words
from collections import Counter

def possibleWords(input, charSet):
    for word in input:
        dict = Counter(word)
        flag = 1
        for key in dict.keys():
            if key not in charSet:
                flag = 0
        if flag == 1 and len(word)>4:
            print(word)

nltk.download('words')
word_list = words.words()
print("Total list of words",len(word_list))
charSet = ['h', 'e', 'l', 'o', 'n', 'v', 't']
possibleWords(word_list, charSet)