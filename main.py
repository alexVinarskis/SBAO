'''
goldbug.txt 
Edgar Allan Poe - The Gold-bug
https://www.lysator.liu.se/~nisse/misc/gold-bug.pdf

verne.txt
20,000 Leagues Under the Sea 
https://1lib.ch/book/962974/bf765b

Goodnight Mister Tom 
https://1lib.ch/book/1825337/45dd0d
'''

import numpy as np
import os.path

books = ['_goldbug.txt', '_verne.txt', '_tom.txt']    # Add books raw txt here, and REMOVE bookData.npy
bookNames = ['The Gold Bug', '20,000 Leagues Under The Sea', 'Goodnight Mister Tom'] 

####
# Helper functions

def getLetterFrequency(filename):
    # read all lines, WITHOUT \n
    lines = ""
    with open(filename) as f:
        for line in f:
            lines = lines + line
    # force to same case so can compare low to low
    lines = lines.lower()
    # loop over alphabet
    numOccuranses = list()
    for letter in "abcdefghijklmnopqrstuvwxyz":
        numOccuranses.append(lines.count(letter))
    # convert to %
    return np.array(numOccuranses)/sum(numOccuranses)*100

def getWordLength(filename):
    # read all lines, WITHOUT \n ?
    words = []
    with open(filename) as f:
        for line in f:
            # force to same case so can compare low to low
            line = line.lower().replace('\n', '')
            words.extend(line.split(" "))
    # loop over words
    temp = [len(ele) for ele in words]
    return [0] if len(temp) == 0 else [(float(sum(temp)) / len(temp))]

def getAuthorMetrics(book):
    authorStyle = []
    # 1. compute letter frequencies
    letterFrequency = getLetterFrequency(book)
    authorStyle.append(letterFrequency)
    # 2. compute word length
    wordLength = getWordLength(book)
    authorStyle.append(wordLength)
    # 3.... can add more metrics
    return authorStyle

def computeAuthorError(bookData, book):
    E = list()
    for author in bookData:
        authorError = []
        for i in range(len(author)):
            difference_array = np.subtract(author[i], book[i])
            squared_array = np.square(difference_array)
            squared_error_total = sum(squared_array)
            authorError.append(squared_error_total)
        E.append(authorError)
    return E

####
# MAIN PROGRAM

bookData = []

if os.path.exists('bookData.npy'):
    with open('bookData.npy', 'rb') as f:
        bookData = np.load(f, allow_pickle=True)
else:
    for book in books:
        # save each book
        bookData.append(getAuthorMetrics(book))
    np.save('bookData.npy', bookData)

book = 'detect_me.txt'

if os.path.exists(book):
    if os.stat(book).st_size == 0:
        print("No text found. Please place your text in 'detect_me.txt' file, and try again.\n")
    else:
        print("Got text to detect, working...\n")
        metrics = computeAuthorError(bookData, getAuthorMetrics(book))
        combinedMetrics = []
        for metric in metrics:
            # adjust numbers experimentally to adjust weights of differnet metrics
            combinedMetrics.append(metric[0]*0.5 + metric[1]*0.5)
        print('Matching scores in order of books is as follows: [lower is better]')
        print(combinedMetrics)
        print('\nClosest match: ' + bookNames[np.argmin(combinedMetrics)] + "\n")
    
else:
    f = open("detect_me.txt", "x") 
    print("No text found. Please place your text in 'detect_me.txt' file, and try again.\n")