# Anagrams-Game-Python

Introduction
For this project you will be writing a game that lets users guess words that can be made using only the letters of a six-letter base word.

Below is a link to a words.txt file that contains 81486 words, one per line. You will use it as a dictionary of words for this assignment, and only words in that file are considered valid words.

words.txt 

Write a Python program that chooses a 6-letter word at random from the lexicon and displays it to the user in a random, scrambled order. Then let the user guess words of varying lengths that can be formed with the letters of the word. After every guess, respond to the user whether the guess was correct, and add it to the list of words that have been guessed so far. Print results grouped by length of words.

For testing and grading purposes, print the unscrambled base word when the program starts.

Here is a sample execution:

TEST: base word is rubies

sribue: 

12 3-letter words left.
[]
13 4-letter words left.
[]
4 5-letter words left.
[]
4 6-letter words left.
[]

Enter a guess: sire
Correct!

sribue: 

12 3-letter words left.
[]
12 4-letter words left.
['sire']
4 5-letter words left.
[]
4 6-letter words left.
[]

Enter a guess: rebus
Correct!

sribue: 

12 3-letter words left.
[]
12 4-letter words left.
['sire']
3 5-letter words left.
['rebus']
4 6-letter words left.
[]

Enter a guess: shrub
Incorrect or already guessed

sribue: 

12 3-letter words left.
[]
12 4-letter words left.
['sire']
3 5-letter words left.
['rebus']
4 6-letter words left.
[]

Enter a guess: user
Correct!

sribue: 

12 3-letter words left.
[]
11 4-letter words left.
['sire', 'user']
4 5-letter words left.
['rebus']
4 6-letter words left.
[]

Enter a guess: q
['bis', 'bur', 'bus', 'ire', 'res', 'rib', 'rub', 'rue', 'sir', 'sub',
'sue', 'use', 'bier', 'brie', 'burs', 'ires', 'ribs', 'rise', 'rube',
'rubs', 'rues', 'ruse', 'sire', 'sure', 'user', 'biers', 'bries',
'rebus', 'rubes', 'bruise', 'buries', 'busier', 'rubies']
$
User input is underlined and has a yellow background. Display lists of guessed words in alphabetical order. Note that entering the string 'q' quits the program. Print all words at the end of the game.

If the user guesses a word that is not in the word dictionary or repeats a guess, print a message saying that the guess is not correct. You can use the same message for both cases, like:
Incorrect--not in the dictionary or already guessed
You don't have to print a message when the user has guessed all of the words, but you might want to do that because it makes the program work better as a game.

Command-line arguments
In order to make grading (and testing) easier, please use command-line arguments as described below. For these purposes I am not considering the name of the program file (sys.argv[0]) to be a command-line argument.)

• No command-line arguments (length of sys.argv is 1): Run the guessing game with a random six-letter word from the dictionary.

EXAMPLE:
$ python3 hw4.py
TEST: base word is garcon

rnacog:
12 3-letter words left.
[]
5 4-letter words left.
[]
6 5-letter words left.
[]
1 6-letter words left.
[]

Enter a guess: con
Correct!
rnacog:
11 3-letter words left.
['con']
5 4-letter words left.
[]
6 5-letter words left.
[]
1 6-letter words left.
[]

Enter a guess: q
['ago', 'arc', 'can', 'car', 'cog', 'con', 'gar', 'nag',
'nor', 'oar', 'rag', 'ran', 'corn', 'crag', 'narc', 'rang',
'roan', 'acorn', 'argon', 'cargo', 'conga', 'groan', 'organ',
'garcon']
• One command-line argument (length of sys.argv is 2): Use the argument (sys.argv[1] as the base word instead of choosing a random six-letter word from the dictionary. I won't use words of any length other than six when grading your program.

EXAMPLE:
$ python3 hw4.py window
TEST: base word is window

idowwn:
9 3-letter words left.
[]
3 4-letter words left.
[]
1 5-letter words left.
[]
1 6-letter words left.
[]

Enter a guess: down
Correct!
idowwn:
9 3-letter words left.
[]
2 4-letter words left.
['down']
1 5-letter words left.
[]
1 6-letter words left.
[]

Enter a guess: q
['din', 'don', 'ion', 'nod', 'now', 'own', 'win', 'won', 'wow', 'down',
'wind', 'wino', 'widow', 'window']
I will be running your program from a Python script and redirecting the input, so please don't ask for any user input other than what is shown in the examples. You might find it helpful to use input redirection when testing your program.

itertools.permutations
You may find the following function from the itertools module helpful:

permutations(iterable [, size])
This function returns an iterator that yields each permutation of the input sequence. For example:

>>> itertools.permutations("abc")

>>> p = itertools.permutations("abc")
>>> for x in p: print x
... 
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
You can also specify a second parameter, which will give you all permutations from the set of that size:

>>> p = itertools.permutations("abc",2)
>>> for x in p: print x
... 
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')
Be sure to read the documentation for itertools.permutations. Also, note that the output from each iteration is a tuple. You will need to convert the tuple of characters to a string (use str.join).

Notes

• Here is a link to a Python documentation page about sorting: http://docs.python.org/3/howto/sorting.html 
You'll want to read up to, and including, the section named Sort Stability and Complex Sorts. You don't need to read the sections about the old ways of sorting. 
You can take advantage of the fact that Python uses stable sort algorithms. That means that if you want words sorted by length and alphabetically, you can first sort them alphabetically and then sort them by length, which is easier than trying to specify primary and secondary sort keys.

• When I run your program, all user input will be lower case.

• When you read each word from the word file, you will need to strip off the newline characters. You can use the strip() method of the string class to do that, but do not pass a parameter to it. With no parameter, it will strip off white space characters, which is exactly what we want. If you pass a parameter, there might be problems using files with different line endings (Unix vs. Windows), but if you don't pass a parameter it will work correctly with any line endings.
