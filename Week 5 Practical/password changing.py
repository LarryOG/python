username = input('Enter your username: \n')
student_ID = input('Enter your student ID: \n')

while 1:
    password = input('Enter password: \n')
    banned_words = [username,student_ID,'huddersfield',
                    'justinbieber','cheese','canalside']

    if len(password) in range (6,13):
        if password in banned_words:
            print('Password too simple. Try different one.')
        else:
            password2 = input('Enter password again: \n')
            if password != password2:
                print ('Passwords do not match. Please try again.')
            else:
                print ('Password changed.')
                break
    else:
        print('Password lenght is invalid. Please try again.')






