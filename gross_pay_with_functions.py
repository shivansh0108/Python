def check_for_float(p_input):
    try:
        value = float(p_input)
        return value
    except ValueError:
        print("Error, please enter numeric input ") 
        quit() 
     
    
def compute_pay(hour, rate):
    if hour < 40:
        pay = round(hour*rate,2)
    else:
        overtime = hour - 40
        pay = round(40 * rate + overtime * rate * 1.5 ,2)
    return pay

    
p_hour = input("Enter hours: ")
p_hour = check_for_float(p_hour)
p_rate = input("Enter rate: ")
p_rate = check_for_float(p_rate)

output = compute_pay(p_hour, p_rate)
print(f"Pay = {output}")

