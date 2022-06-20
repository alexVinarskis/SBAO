# SBAO
Statistics Based Author Detector

## Intro
This small program was made for ETH course "Science in Perspective: Writing Technology". The goal is to show basic language manipulations task, such as distinguishing between writing styles, can be done without complex ML models, using simple statistics instead.

## Approach
A number of books (or extracts) is recorded in raw text file. The code does pre-processing to create statistical data for each of the books. When running comparison, code recomputes these metric for the extract of the text, and picks most probable match based on least square error approach.

Currently, the following metrics are used, with 50/50 weight:
* Frequency of letters: this technique is usually used to identify the language used. However, given how different writing styles of authors (especially if texts are from different centuries) are, this may be usefull to identify between modern/classical/slang English.
* Average word length: this (should) help to distinguish between type of text, such as scientific writing, descriptive, direct speech, etc.

## Instructions
* Clone this repo
* Run program once to create files and follow the instructions. You will be required to paste a text fragment (~paragraph) of the book in a `.txt` file, so the program can pick it up. 

Currently, samples of three books were taken. Follow instructions inside of `main.py` to add more. 
Similarly, additional metrics can be easily added, and their weights can be altered. 