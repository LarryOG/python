try:
    number_of_students = int(input('Enter the number of students in the class: '))
    if number_of_students <=0:
        print('Invalid number of students. Try again!')
        raise SystemExit
    number_of_PCs = int(input('Enter the number of PCs in the lab: '))
    if number_of_PCs <=0:
        print('really? Stop fooling around...')
        raise SystemExit
    if number_of_PCs > number_of_students:
        print('You need 1 lab for all the students.')
    else:
        number_of_labs = number_of_students // number_of_PCs
        left = number_of_students % number_of_PCs
        if left > 0:
            number_of_labs = number_of_labs + 1
        print('You need ',number_of_labs,' labs for all the students')

except ValueError:
    print('Enter valid amount, please.')

