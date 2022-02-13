from math import log2

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

def filter_list(words, results, guess):
    if len(guess) != 5:
        raise ValueError("Length of guess must be 5")
    if len(results) != 5:
        raise ValueError("Length of results must be 5")

    wordList = words.copy()
    filteredWords = wordList.copy()
    inWord = ""

    for i in range(5):
        if results[i] == "G":
            inWord = inWord + guess[i]
            for j in range(len(wordList)):
                if guess[i] != wordList[j][i]:
                    filteredWords.remove(wordList[j])
            wordList = filteredWords.copy()

    for i in range(5):
        if results [i] == "Y":
            inWord = inWord + guess[i]
            for j in range(len(wordList)):
                if (guess[i] not in wordList[j]) or (guess[i] == wordList[j][i]):
                    filteredWords.remove(wordList[j])
            wordList = filteredWords.copy()
    for i in range(5):
        if results[i] == "B":
            for j in range(len(wordList)):
                if (guess[i] in wordList[j]) and (guess[i] not in inWord):
                    filteredWords.remove(wordList[j])
            wordList = filteredWords.copy()
    return filteredWords

def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def get_avg_bits(words,guess):
    avgNewWords = 0
    baseMap = {
        0:"B",
        1:"Y",
        2:"G"
    }
    for i in range(243):
        numbers = number_to_base(i,3)
        while len(numbers) < 5:
            numbers = [0] + numbers
        letterInput = []
        for num in numbers:
            letterInput.append(baseMap[num])
        avgNewWords += len(filter_list(words,letterInput,guess))
    p = (avgNewWords/243)/len(words)
    bits = log2(1/p)
    return bits

def select_best_guess(wordList):
    bestGuess = "ERROR"
    highestBits = 0
    for guess in wordList:
        if get_avg_bits(wordList,guess) > highestBits:
            bestGuess = guess
            highestBits = get_avg_bits(wordList,guess)
    return bestGuess
