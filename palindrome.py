#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

curFile = open("words.txt")

palindromeCount = 0

for curLine in curFile:
    text = curLine.strip().lower()

    if text == text[::-1]:
        palindromeCount += 1
curFile.close

print("Number of palindromes:", palindromeCount)