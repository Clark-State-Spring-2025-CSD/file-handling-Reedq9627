#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

count = 0
sum = 0
highNum = None
lowNum = None

curFile = open("numbers.txt")

for curLine in curFile:
    number = int(curLine.strip())
    count += 1
    sum += number

    if highNum is None or number > highNum:
        highNum = number
    if lowNum is None or number < lowNum:
        lowNum = number

if count > 0:
    average = sum / count
else:
    average = 0
curFile.close()

print("Total numbers:", count)
print("Sum of numbers:", sum)
print("Average:", average)
print("Highest number:", highNum)
print("Lowest number:", lowNum)


