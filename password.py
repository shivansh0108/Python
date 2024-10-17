def password_controller(password):
    if len(password) > 8:
        return True
    else:
        return False

result = password_controller("assaulter#1892")   
print(result) 

