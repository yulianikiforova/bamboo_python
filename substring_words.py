#Given a dictionary and a string,
#find all the substrings that are valid words in dictionary.
def substring_words(dictionary_of_words, word):
    list_of_words = []
        for i in range(len(word)):
            for j in range(len(word)):
                if i + j <= len(word) and i != i+j:
                     if word[i:i+j] in dictionary_of_words:
                         list_of_words.append(word[i:i+j])
        return list_of_words
