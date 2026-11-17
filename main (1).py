print("+-----------------------------------------------------------------+")
print("|          Welcome to my simple PYTHON TUTORIAL LEARNING          |")
while True:
    # Lines 1 to 7: Main Menu
    print("+-----------------------------------------------------------------+")
    print("| [1] | - Prelim Lesson                                           |") 
    print("| [2] | - MidTerm Lesson                                          |") 
    print("| [3] | - Finals Lesson                                           |") 
    print("| [4] | - Exit                                                    |")
    print("+-----------------------------------------------------------------+")
    
    try:
        user = int(input("| Choose Lesson (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        print("+-----------------------------------------------------------------+")
        continue
        
    print("+-----------------------------------------------------------------+")
    
    if user == 1:
        while True:
            print("| [1] - Chapter 1 - Introduction to programming") 
            print("| [2] - Chapter 2 - Python Basic Syntax") 
            print("| [3] - Chapter 3 - Arithmetic Operators And Expressions") 
            print("| [4] - Chapter 4 - Basic Input and Output in Python")
            print("| [5] - Back to the main menu ")
            break
            
        print("+---------------------------------------------------")
        user1 = input("| Choose Chapter 1-5: ")
        print("+-------------------------------------------------------")
        
        if user1 == '1':
            print("|      What is Programming languages")
            print("|   A programming languages is a special languages that")
            print("|   computers understood and use to understand and use to perform tasks.")
            print("|   Such as:            ")
            print("|   Python C++ PHP JAVA and etc")
            print("|   these coding language isnt just for usable things ")
            print("|   it just ")
            print("|")
            print("|      What is Python Programming")
            print("|   Python is a widely-used programming language that was")
            print("|   created by Guido Van Rossum in 1991")
            print("+-----------------------------------------------------------------+")
            input("| Chapter 1 finished! Press Enter to return to the main menu... ")
            print("|")
            continue
            
        elif user1 == '2':
            print("|     What is Python Syntax?")
            print("|  Syntax refers to the set of rules")
            print("|  that tell us how to correctly write ")
            print("|  a program in Python.")
            print("|     Is it hard?")
            print("|     Not that really hard just pure understanding the lesson.")
            print("+-------------------------------------------------------------")
            print("|     PYTHON SYNTAX ")
            print("|  1. Python is Case-Sensitive - ")
            print("|     Python treats uppercase and lowercase letters differently")
            print("|  2. Indentation -")
            print("|     Unlike other programming languages. Python uses Indentation")
            print("|     (spaces) to define blocks of code.")
            print("|     Example: age = 18")
            print("|     if age >= 18:")
            print("|        print('Adult')")
            print("+-----------------------------------------------------------------+")
            
            user3 = input("|   Would you like to take a little activity? (Y/N) : ")
            if user3.lower() == 'N':
                print("|")
                print("|               RETURNING TO THE MAIN MENU              ")
                print("|")
                continue  # Jumps straight back to lines 1-7
                
            print("|     Now you try")
            print("|     age = 15")
            print("|     if age _= 18:")
            print("|        print('Teenager')")
            print("| ")
            print("|     What would you put?")
            print("|   A. <  B. >  C. =  D. ?")
            
            user2 = input("|   What would be your choice? Think wisely 🧐: ")
            print("| ")
            
            if user2.upper() == 'A':
                print("|    YOURRRRR RIGHTTTTTTTTT")
            elif user2.upper() == 'B':
                print("|   Not quite but nice try!")
            elif user2.upper() == 'C':
                print("|   Nice try! ^-^")
            elif user2.upper() == 'D':
                print("|   Maybe try again?")
                
            print("+------------------------------------------------------------------+")
            
            user4 = input("|   Would you like to continue the whole chapter? (Y/N): ")
            print("+------------------------------------------------------------------+")
            if user4.lower() == 'N':
                print("|           Returning to main menu")
                print("|")
                continue  
            print('\n' * 30)    
            print("|      PRINTING TEXT")
            print("|   Text (also called a string) must be enclosed in")
            print("|   quotation marks.")
            print("|   ")
            print("|   Example: print(Adult) <---- This is wrong ❌")
            print("|            print('Adult') <---- This is Right ✅")
            print("|   Now we will continue through all the chapter you chose")
            print("|   ")
            print('\n' * 30)
            print("|   Variables, Constants, and Data Types in Python")
            print("|")
            print("|   1. What is a Variable?")
            print("|      A variable is a named storage location used to keep data in a program.") 
            print("|      The value of a variable can change while the program is running. ")
            print("|      Example: a, b, c, age, name")
            print("|   ")
            print("|    A variable name must start with a letter or the underscore character  ")
            print("|      ✅ - age = 20   _value = 100  total = 50 ")
            print("|      ❌ - 1stValue = 10  2total = 30  123name = 'john' ")
            print("|      ")
            print("|      Variable Naming Rules:")
            print("|      (age and AGE are two different variables)")
            print("+-------------------------------------------------------------------   ")
            activity1 = str(input("| Would u like to take another activity? (Y/N): "))
            if activity1 == 'Y':
                print('\n' * 30)
                print("+--------------------------------------------------------------")
                print("|                           Now you try!")
                print("|")
                print("|                IF THE VARIABLE STARTS AT 9input is it true or false?")
                print("|     A. True    B. False ")
                answer = str(input("|     What will be your answer? (A/B): "))
                if answer.upper() == 'B':
                  print("|      YOURRRRR RIGHTTTTTTTTT")
                elif answer.upper() == 'A':
                  print("|     Not quite but nice try!")
            input("| Press Enter to continue the chapter                       |")
            import time
            for i in range(1, 6):
                print(f"|       {i}")
                time.sleep(1)
            print("+---------------------------------------------------------------------- ")
            print("|      Output Variables")
            print("|      The Python print() function is often used to output variables.")
            print("|      example: a = 'I'")
            print("|               b = 'Love'")
            print("|               c = 'Her'")
            print("|               print(a, b, c)")
            print("|               Output: I Love Her")
            print("| ")
            print("|      In the print() function, you output multiple variables, or")
            print("|      seperated by a +:")
            print("       example: z = 'I'")
            print("|               x = 'Love'")
            print("|               v = 'Her'")
            print("|               print(a + b + c)")
            print("|               Output: I Love Her")
            print("+---------------------------------------------------------------        ")
            choice = str(input("Would you like to continue? (Y/N): "))
            if choice == 'Y':
                print('\n' * 30)
            elif choice == 'N':
              continue
            import time
            for i in range(1, 6):
                print(f"|       {i}")
                time.sleep(1)
            print("+---------------------------------------------------------------   ")
            print("|                BASIC DATA TYPES IN PYTHON  ")
            print("|      Data Types - ")
            print("|      Data types are categories that tell Python what kind of data a")
            print("|      variable stores. They determine the type of value a variable can")
            print("|      hold and what operations can be performed on that value.")
            print("|      Examples: ")
            print("|      int - is for numbers (10, 99, 20, -99")
            print("|      float - is for decimal numbers (10.1 , 9.19, 20.01, -99.5")
            print("|      str - is for text or string ('June', 'May', 'July'")
            print("|      bool - represent as True or false (True, false) ")
            print("|      example:           ")
            print("|      name = 'maria'      #string")
            print("|      age = '21'          #integer")
            print("|      grade = 89.5        #decimal")
            print("|      is_enrolled = True  #boolean")
            print("+---------------------------------------------------------------   ")
            print('\n' * 30)
            print("+---------------------------------------------------------------   ")
            print("|      Now lets do a little quiz about the lesson you chose")
            
            
            
            print("+-----------------------------------------------------------------+")
            input("| Chapter 2 finished! Press Enter to return to the main menu... ")
            print("|")
            continue
            
        elif user1 == '3':
            print('\n' * 30)
            print("+-----------------------------------------------------------------+")
            print("|                     Arithmetic Operators")
            print("|    What are the arithmetic operators?")
            print("|    Arithmetic operators are symbols used to perform mathematical")
            print("|    calculations on numbers. They work the same way as the operators")
            print("|    used in everyday mathematics.")
            print("|                  Python Arithmetic Operators")
            print("|     + Addition ","         4+4 = 8", "               - Subtraction", " 21-5 = 16")
            print("|     * Multiplication","    6 * 10 = 60 ", "          / Division", "20 / 4 = 5.0")
            print("|     // Floor division", "   24 // 5 = 8", "           % Modulus", "10 % 3 = 1")
            print("|     ** Exponentiation ", "  3 ** 3 = 27")
            print("+-----------------------------------------------------------------+")     
            print("|                   Expressions in Python   ")
            print("|     It is an expression is a combination of values, variables,")
            print("|     and operators that evaluates to a result.          ") 
            print("|     example:")
            print("|     a = 3               # first number")
            print("|     b = 4               # second number")
            print("|     result = a * b      # add the numbers      ")            
            print("|     output = 12          ")
            print("+-----------------------------------------------------------------+")
            input("| Chapter 3 finished! Press Enter to return to the main menu... ")
            print("|")
            continue
            
        elif user1 == '4':
            print('\n' * 30)
            print("+-----------------------------------------------------------------+")
            print("|   Accepting User Input") 
            print("|   • Purpose of input in programming Real-life analogies")
            print("|     (e.g., asking for a user's name and responding)")
            print("|    Using input() functionSyntax:")
            print("|    Syntax: variable = input('Prompt message:')")
            print("|    All input is string type by default")
            
            print("|   for example:")
            print("|   age = input('Enter your age:')")
            print("+-----------------------------------------------------------------+")
            print("|   Formatting Output")
            print("|   Using comma , in print():            ")
            print("|               ")
            print("|   age = input('Enter your age:')")
            print("|   name = input('Enter your name:')")
            print("|   print('name:', name)            ")
            print("+-----------------------------------------------------------------+")
            input("| Chapter 4 finished! Press Enter to return to the main menu... ")
            print("|")
            continue
            
        elif user1 == '5':
            continue
        else:
            print("Invalid Choice :<")
            print("|")
            continue
            
    elif user == 2:
          while True:
              print("+-----------------------------------------------------------------+")
              print("| [1] - Chapter 1 -   Conditional Statements in Python            |") 
              print("| [2] - Chapter 2 -   LOGICAL OPERATOR                            |") 
              print("| [3] - Back to the main menu                                     |")
              break
            
          print("+-----------------------------------------------------------------+")
          user1 = input("| Choose Chapter 1-3: ")
          if user1 == '1':
            print('\n' * 30)
            print("+-----------------------------------------------------------------+")
            print("|             Introduction to Conditional Statements              |")
            print("|     • A condition statement allows a program to make decision   |")
            print("|       based on whether a condition is True or False             |")
            print("|                                                                 |")
            print("|     Example: age = 18                                           |")
            print("|     if age >= 18:                                               |")
            print("|        print('Adult')                                           |")
            print("+-----------------------------------------------------------------+")
            print("|    Operator    Meaning                  Example      Result     |")
            print("|       ==       Equal to                 5 == 5        True      |")
            print("|       !=    Not Equal to                6 != 5        True      |")
            print("|        >     Greater than               6 > 5         True      |")
            print("|        <       Less than                5 < 10        True      |")
            print("|       >=   Greater than or equal to     10 >= 10      True      |")
            print("|       <=   Less than or equal to        5 <= 10       True      |")
            print("+-----------------------------------------------------------------+")
            input("|                Press Enter to take a QUIZ  ")
            print('\n' * 30)
            print("|  QUIZ")
            print("|  1: Easy")
            print("|  2: Medium")
            print("|  3: Hard")
            print("|  4: Insane")
            choose = int(input("Choose an difficulty: "))
            if choose == '1':

            elif choose == '2':
              
            elif choose == '3':

            elif choose == '4':
            input("| Chapter 1 finished! Press Enter to return to the main menu... ")
            print("|")
            
            continue
            
              

      
        
    elif user == 3:
        print("Finals Lesson selected.")
        input("| Press Enter to return to the main menu... ")
        print("|")
        continue
    elif user == 4:
        print("|                     Thank you for choosing me!                  |")
        break
    else:
        print("Invalid Choice :<")
        print("|")
        continue