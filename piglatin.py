#!/usr/bin/env python2.7
word_list = []
valid_word = False
index = -1
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
vowel_found = False

#requesting and verfying if the word is valid
word = raw_input('Please enter a word:')
while valid_word == False:
    if word.isalpha():
        #print 'valid word'
        valid_word = True
    else:
        word = raw_input('Not a valid word, try again:')

#converting string to list for comparison
for i in range(0, len(word)):
    word_list.append(word[i])

#find's index for first vowel
for i in word_list:
    if vowel_found == False:
        for x in vowels:
            #print 'i', i
            #print 'x', x
            if i == x:
                vowel_found = True
                break
        index += 1
    else:
        #print vowel_found
        #print index
        break

#creates the pig latin word
word = word + word[0:index] + 'ay'
word = word[index:len(word)]
print word
