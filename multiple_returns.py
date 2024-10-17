def format_name(fname, lname):
    if fname == "" or lname == "":
            return "First name or the last name cannot be empty"
    format_fname = fname.title()
    format_lname = lname.title()
    return f"{format_fname},{format_lname}"

first_name = input("Enter First name: ")
last_name = input("Enter Last name: ") 
output = format_name(first_name,last_name)
print(output)


