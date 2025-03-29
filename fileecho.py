#Read in the echo.txt file and display it in the terminal using print()
#This is a guided practice. Either follow the video or your instructor in class.

curFile = open("echo.txt")
for curLine in curFile:
    print(curLine)
curFile.close()

# print(curLine)