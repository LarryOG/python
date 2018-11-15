

def left_part_of_email (email):
    print(email.split('@')[0])


some_email = input('Enter an Email: ')
left_part_of_email(some_email)