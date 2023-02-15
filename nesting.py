#nesting 

# for/While/

# if/else

# switch
# case:

# Algorithms/FlowChart

# Process to become Azubian 50 students

# 1. Call for applications
# 2. Take applications 30 150 while loop
# 3. Evaluate applications occupation == doctor
# 4. MAke a selection 75
# 5. Interviews for loop
# 6. MAke selection case 1: completed an online program case 2: understand leadership values default
# 7. Send out admissions 60 for

#spanish english japanese
def nesting():
    confirm = ""
    languages = ["English", "Japanese", "Spanish"] ## english, spanish, japanse, german, manadrin
    while confirm != "Y":
        startV = str(input("Do you want to start the application"))
        confirm = startV
    userInput = str(input("Please enter your name: "))
    userInputClass = str(input("Please language "))
    
    if userInput == "Rahab":
        print("Welcome to class ", userInput)
        for language in languages:
             if userInputClass == language:
                print("Your instructor is Joseph")
             
             else:
                print("Sorry the language you entered is uanavailabe at the moment")
           
    else:
        print("This is not your class ", userInput)


nesting()

# 