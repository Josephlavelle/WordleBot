def get_results(guess: str):
    print(guess)
    response_array = []
    response = ""
    while len(response) !=5:
        response = input("Input Wordle Results (B = Black, G = Green, Y = Yellow)\n")
        ##
        ## will need to catch Error If response is not BGY compatible
        ##
    for letter in response:
        response_array.append(letter)
    return response_array

def filterList(words, results, guess):
    wordList = words
    if len(guess) != 5:
        raise ValueError("Length of guess must be 5")
    if len(results) != 5:
        raise ValueError("Length of results must be 5")
    for i in range(5):
        filteredList = []
        if results[i] == "G":
            for j in range(len(wordList)):
                if guess[i] == wordList[j][i]:
                    filteredList.append(wordList[j])
        elif results [i] == "Y":
            for j in range(len(wordList)):
                if guess[i] in wordList[j] and guess[i] != wordList[j][i]:
                    filteredList.append(wordList[j])
        elif results[i] == "B":
            for j in range(len(wordList)):
                if guess[i] not in wordList[j]:
                    print(guess[i])
                    print(wordList[j])
                    filteredList.append(wordList[j])
        wordList = filteredList
    return list(wordList)

