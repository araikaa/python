def check_pass(pas):
    a=int(0)
    if (len(pas)==8):
        if any(c for c in pas if c.islower()):
            if any(c for c in pas if c.isupper()):
                if '-' in pas or '*' in pas or '#' in pas:{
                 print('Your password is perfect')
                }
                else:{
                    print('Password has no such elements like "*-#')
                 }
            else:{
                print('Password has no any uppercase characters')
            }
        else:{
        print('Password has no any lowercase characters')
        }
    
    else:{
        print('Password has less than 8 characters or more')
    }
    
check_p=input('Please enter your password: ')
check_pass(check_p)
