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
    while confirm != "Y":
        startV = str(input("Do you want to start the application(Y/N): ").upper())
        confirm = startV
    else:
        userInput = str(input("Please enter your name: "))
        users = ["Rahab", "Kwasi", "Elizabeth", "Kwame", "Prince"]  
        i = 0
        while i < len(users):
            userName = users[i]
        i = i + 1  
        if userName == userInput:
            print("Welcome to class ", userInput)
        else:
            print("This is not your class,", userInput)
             
#@TODO: First determine is the languague enetered by the user is in our collection. If it is assign an instructor, if it is not but is offered assign another instructor. If it is not offered print out a message.
         #   languages = ["English", "Japanese", "Spanish"] ## english, spanish, japanse, german, mandarin
          #  languages1 = ["German", "Mandarin"]
           # allLang = languages + languages1
            #for language in languages:
             #   userInputClass = str(input("Please enter language: "))
              #  if userInputClass == language:
               #     print("Your instructor is Joseph")
                    
                #elif userInputClass == languages1:
                 #   print("Your instructor is Ajara")
                        
                #else:
                 #   print("Sorry the language you entered is uanavailabe at the moment")
           
        


nesting()