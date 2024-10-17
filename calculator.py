def calculator (f_num:int, s_num:int, choice):
    
    if choice == "+":
        sum = (f_num) + (s_num)
        return sum
    elif choice == "-":
        substract =(f_num) - (s_num)
        return substract
    elif choice == "*":
        multiple =(f_num) * (s_num)
        return multiple
    elif choice == "/":
        divide = (f_num) / (s_num)
        return divide
    # else:
    #     return "Bye"

first_num = input("Enter you first number: ")
second_num = input("Enter you second number: ")     
user_choice = input("Enter you choice of Operation: ")
if first_num =='' or second_num =='' or user_choice =='':
        # raise ValueError("Please provide a valid input !!")
    print ("Please enter a valid value !!")
else:  
    output = calculator(int(first_num), int(second_num), user_choice)
    print(output)