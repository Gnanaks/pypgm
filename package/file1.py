#function 1---valid username

def valid_username(a):
    if '_' in a:
        return "valid username"
    else:
        return "invalid username"
    print(valid_username)

#function 2---valid password
def valid_password(pw):
    uc = 0
    lc = 0
    dig = 0
    sc = 0

    for i in pw:
        if 'A' <= i <= 'Z':
            uc += 1
        elif 'a' <= i <= 'z':
            lc += 1
        elif '0' <= i <= '9':
            dig += 1
        else:
            sc += 1

    if uc >= 2 and lc >= 2 and dig >= 2 and sc >= 2:
        return 'valid password'
    else:
        return 'Invalid password'