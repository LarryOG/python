username = input('Enter your username: \n')
student_ID = input('Enter your student ID: \n')

password = input('Enter password: \n')
password2 = input('Enter password again: \n')

banned_words = [username,student_ID,'huddersfield','justinbieber','cheese','canalside']

if password == password2:
    if len(password)>5 and len(password)<=13:
         if password in banned_words:
             print('You need to use different password')
         print('Password Changed')
