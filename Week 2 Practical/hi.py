
try:
    number_of_pupils = int(input('Provide number of pupils: '))

    number_of_sweets = int(input('Provide number of sweets: '))

    if number_of_pupils > 0 and number_of_sweets > 0:
        sweets_per_pupil = number_of_sweets // number_of_pupils

        left_over = number_of_sweets % number_of_pupils


        print('Sweets per pupil', sweets_per_pupil,'\nSweets left for the teacher', left_over)
    elif number_of_pupils == 0:
        print('There are no pupil to share the sweets between.\n Sweets left for the Teacher:', number_of_sweets)
    elif number_of_sweets == 0:
        print('There are no sweets to share')
    else:
        print('negative integer')
except ValueError:
    print('Enter integer')