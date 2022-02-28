#import wordle list and alphabet list
from lists import wordle, alphabet
#count will store number of occurances of each character
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#for loops to count occurance of each character in wordle list
for word in wordle:
    word_list = list(word)
    for letter in word_list:
        n = alphabet.index(letter)
        count[n] += 1

#store count list into new list, sorted from largest number to smallest
count_sorted = sorted(count, reverse=True)

#to store top 4 occurring characters
#why not 5? there are no full words which contain all 5 of the most common characters
letter_set = []
for num in count_sorted[0:4]:
    letter_set.append(alphabet[count.index(num)])

#find words which contain all characters in letter_set[]
m = 0
top_words = []
for word in wordle:
    match = len(set(list(word)) & set(letter_set))
    if match == 4:
        top_words.append(word)
    m += 1

#same process as above if there are no "hits" on the first word
letter_set = []
for num in count_sorted[4:8]:
    letter_set.append(alphabet[count.index(num)])

m = 0
second_choice = []
for word in wordle:
    match = len(set(list(word)) & set(letter_set))
    if match == 4 and len(set(top_words[0]) & set(top_words[1]) & set(top_words[2]) & set(list(word))) == 0:
        second_choice.append(word)
    m += 1

#could continue the above but seems inefficient and probs a cleaer way to do it

#print statements
print(alphabet)
print(count)
print(letter_set)
print("Best probability starters: ", top_words)
print("If no hit on first: ", second_choice)

# adore, arose, opera
# split, spilt