def isIsogram(word):

    for letter in word:
    #Iterates through each letter and counts occurences
        if word.count(letter) > 1:
            return False       #Returns False if letter occurs more than once
    return True     #Returns True if all letters occur only once

validInput = False

#This block repeats until a valid word is entered
while not validInput:
    #Get word to test
    word = input("Please enter a word to test: ")
    if word.isalpha():
        validInput = True
    #Check for valid input
    if not word.isalpha():
        print("Last time I checked, words didn't contain numbers...")


#This code runs if isIsogram() returns True
if isIsogram(word.lower()):
    print(word, "is an isogram.")
#This code runs if isIsogram() returns False
else:
    print(word, "is not an isogram.")
