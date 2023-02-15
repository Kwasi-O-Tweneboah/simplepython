from functions import calculateTax, readFile, writeFile, currentWorkingDirectory
import math


#@TODO: Refactor code to also accept user name.

inputName = str(input('Please enter your name: '))
userInput = int(input('Please amount: '))
bill = calculateTax(userInput)
print("Total amount to be paid is: " , bill)
print("This is the floored bill " , math.floor(bill))
readFile(inputName)
writeFile(inputName, bill)
currentWorkingDirectory()
