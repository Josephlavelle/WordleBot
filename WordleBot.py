import csv
from wordle_bot_functions import *

# Import Words
with open('wordle-allowed-guesses.txt') as f:
    lines = f.readlines()
wordList = []
for word in lines[0:-1]:
    wordList.append(word[0:-1])
wordList.append(lines[-1])

with open('wordle-answers.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    answerList = list(csv_reader)

guess = "crane"
state = "BBBBB"
guesses = 0
filteredList = wordList
while state != ["G","G","G","G","G"]:
    guesses += 1
    results = get_results(guess)
    state = results
    print(state)
    filteredList = filter_list(filteredList,results,guess)
    print("filtered")
    ### Retrieve new guess from List -- Will need to incorporate Bits
    guess = select_best_guess(filteredList)
    print("Guess Selected")
    
print("________________________________\n\nYou won in " + str(guesses) + " guesses!\n________________________________")