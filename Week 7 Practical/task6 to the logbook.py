import sys, random


def email_at_domain (domain, email):
    if email.count('@') != 1 or email[0] == '@' or email.split('@')[1] != domain:
        print('Email ', email, ' is not valid at ', domain)
        raise SystemExit
    else:
        print('Email ', email, ' is valid at ', domain )


def random_pick(some_list):
    return random.choice(some_list)


def left_part_of_email(email):
    return email.split('@')[0]


def one_in_another (question, word):
    is_it_inside = word in question
    return is_it_inside


def random_exit():
    percentage_chance = 15

    if random.randint(0, 100) < percentage_chance:
        raise SystemExit


DOMAIN = 'pop.ac.uk'
NAMES = ['Tom', 'John', 'Adam', 'Adrian', 'Daniel', 'Joseph', 'Martin', 'Peter']
DICTIONARY = {
                1: 'The library is closed today.',
                2: 'WiFi is excellent across the campus.',
                3: 'Your deadline has been extended by two working days.'
                }
RANDOM_RESPONDS = ['Maybe', 'Tell me more', 'I am pleased to hear that.',
                   'You have to be more specific', 'Try me', 'Really?']


user_email = input('Enter email: ')
email_at_domain(DOMAIN, user_email)


print('Hi', left_part_of_email(user_email).capitalize(), 'my name is ',
      random_pick(NAMES), ' How can I help you today?')
while 1:
    user_question = input(' ')
    ending_line = 'goodbye'

    if user_question.lower() == ending_line.lower():
        break
    elif one_in_another(user_question, 'library'):
        print(DICTIONARY.get(1))
        random_exit()
    elif one_in_another(user_question, 'WiFi'):
        print(DICTIONARY.get(2))
        random_exit()
    elif one_in_another(user_question, 'deadline'):
        print(DICTIONARY.get(3))
        random_exit()
    else:
        print(random_pick(RANDOM_RESPONDS))
        random_exit()