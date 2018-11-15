import sys
import random

def email_at_domain (domain, email):
    if email.count('@') != 1 or email[0] == '@' or email.split('@')[1] != domain:
        print('Email ', email, ' is not valid at ', domain)
        raise SystemExit
    else:
        print('Email ',email, ' is valid at ', domain )


def random_pick (some_list):
    import random
    return random.choice (some_list)


def left_part_of_email (email):
    return email.split('@')[0]


def one_in_another (question,word):
    is_it_inside = word in question
    return is_it_inside


DOMAIN = 'pop.ac.uk'
NAMES = ['Tom', 'John', 'Adam', 'Adrian', 'Daniel', 'Joseph', 'Martin', 'Peter']
WORDS = ['library','WiFi','deadline']
RANDOM_RESPONDS = ['Maybe', 'Tell me more', 'I am pleased to hear that.', 'You have to be more specific','Try me','Really?']
PERCENTAGE_CHANCE = 15


user_email = input('Enter email: ')
email_at_domain(DOMAIN,user_email)


print('Hi', left_part_of_email(user_email), 'my name is ', random_pick(NAMES), ' How can I help you today?')
while 1:
    user_question = input(' ')
    ending_line = 'goodbye'

    if random.randint(0,100) < PERCENTAGE_CHANCE:
        raise SystemExit
    else:

        if user_question.lower() == ending_line.lower():
            break
        elif one_in_another(user_question,WORDS[0]):
            print('The library is closed today.')
        elif one_in_another(user_question,WORDS[1]):
            print('WiFi is excellent across the campus.')
        elif one_in_another(user_question,WORDS[2]):
            print ('Your deadline has been extended by two working days.')
        else:
            print(random_pick(RANDOM_RESPONDS))