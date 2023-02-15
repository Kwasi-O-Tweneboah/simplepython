from functions import calculateTax, readFile, writeFile, currentWorkingDirectory
import math


#@TODO: Refactor code to also accept user name.

userName = str(input('Please username: '))
userInput = int(input('Please amount: '))

bill = calculateTax(userInput)
print("Total amount to be paid is: " , bill)
print("This is the floored bill " , math.floor(bill))
readFile(userName)
writeFile(bill, userName)
currentWorkingDirectory()
