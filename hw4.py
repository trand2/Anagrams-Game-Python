import sys, random, itertools

sixLetterWords = []
allWords = []
selectedWord = ""
with open("words.txt") as fin:
    for line in fin.readlines():
        for word in line.split():
            allWords.append(word)
            if len(word) == 6:
                sixLetterWords.append(word)
if len(sys.argv) == 1:
    selectedWord = random.choice(sixLetterWords)
elif len(sys.argv) == 2:
    if sys.argv[1] in sixLetterWords:
        selectedWord = sys.argv[1]
    else:
        print("Not a valid word. Please try again.")
        quit()
else:
    print("Too many command line arguments. Please try again.")

print("TEST: base word is {}\n".format(selectedWord))

mixedWordList = []
p = itertools.permutations(selectedWord)
for x in p:
    tupStr = ''.join(x)
    if tupStr != selectedWord:
            mixedWordList.append(tupStr)

scrambledWord = random.choice(mixedWordList)
mixedWordList.remove(scrambledWord)
print('{}:\n'.format(scrambledWord))

possiblePermutations = []
guessedPermutations = []
guessedPermutations1 = []
guessedPermutations2 = []
guessedPermutations3 = []


for x in range(len(selectedWord)-3, len(selectedWord)+1):
    p = itertools.permutations(selectedWord, x)
    i = 0
    for y in p:
        tupStr1 = ''.join(y)
        if tupStr1 in allWords:
            # print(tupStr1)
            possiblePermutations.append(tupStr1)
            allWords.remove(tupStr1)
            i += 1

    print("{} {}-Letter words left".format(i, x))
    print("[]")

print()


def permutations(guesses):
    for z in range(len(selectedWord) - 3, len(selectedWord) + 1):
        counter = 0

        if guesses in possiblePermutations and z == len(guesses):
            possiblePermutations.remove(guesses)
            if z == len(selectedWord)-3:
                guessedPermutations.append(guesses)
            elif z == len(selectedWord)-2:
                guessedPermutations1.append(guesses)
            elif z == len(selectedWord)-1:
                guessedPermutations2.append(guesses)
            elif z == len(selectedWord):
                guessedPermutations3.append(guesses)

        for a in possiblePermutations:
            if len(a) == z:
                counter += 1
                
        print("{} {}-Letter words left".format(counter, z))

        if z == len(selectedWord)-3:
            print(guessedPermutations)
        elif z == len(selectedWord)-2:
            print(guessedPermutations1)
        elif z == len(selectedWord)-1:
            print(guessedPermutations2)
        elif z == len(selectedWord):
            print(guessedPermutations3)

    print()


while True:
    guess = input("Enter a guess: ")
    if guess == "q":
        break
    else:
        if guess in possiblePermutations:
            print("Correct!\n")
            print('{}:\n'.format(scrambledWord))
            print()
            permutations(guess)
        else:
            print("Incorrect or already guessed\n")
            print('{}:\n'.format(scrambledWord))
            print()
            permutations("")

print(sorted(possiblePermutations, key=lambda x: (len(x), x)))
quit()
