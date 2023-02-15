#function to calculate tax

import os

vatRate = 12.5

#function declaration
def calculateTax(amount):
    tax = (amount * vatRate) /100
    totalAmount = tax + amount
    return totalAmount


def readFile(userName):
    #print("This is the beginning of the file handling process")
    file1 = open("file1.txt", "r")
    print("Thank you " + str(userName) + " for your patronage")
    print(file1.read())
    file1.close()


def writeFile(totalAmount, userName):
    try:
        file2 =open("file2.txt", "w")
        file2.write("Total amount for " +str(userName) + " is " + str(totalAmount) )
        file2.close()
    except file2.exception:
        print("There is an error with the file")


def currentWorkingDirectory():
    cwd = os.getlogin()
    print(cwd)