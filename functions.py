#function to calculate tax

vatRate = 12.5

#function declaration
def calculateTax(amount):
    tax = (amount * vatRate) /100
    totalAmount = tax + amount
    return totalAmount


userInput = int(input('Please amount: '))
bill = calculateTax(userInput)
print("Total amount to be paid is: " , bill)