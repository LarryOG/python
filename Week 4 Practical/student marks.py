name = input('Enter the studnet\'s name:')

total_marks = 0
try:

    for i in range (5):
        mark = int(input('Enter student\'s mark: '))
        total_marks += mark

    average_mark = total_marks / 5

    print ('Final Mark for ' + name.capitalize() + ' is ' + str(average_mark))



except ValueError:
    print ('Enter a number, please')


