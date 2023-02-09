#Lukasz Grzybek

def valid_password(pswrd):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    if len(pswrd) < 7:
        return False
    var_one = False
    var_two = False
    var_three = False
    for i in pswrd:
        if i in upper:
            var_one = True
        if i in lower:
            var_two = True
        if i in number:
            var_three = True
    if var_one == True and var_two == True and var_three == True:
        return True
    else:
        return False

