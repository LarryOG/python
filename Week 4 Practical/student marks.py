name = input('Enter the studnet\'s name:')
NUMBER_OF_MARKS = 5
total_marks = []
try:

    for i in range (NUMBER_OF_MARKS):
        mark = int(input('Enter student\'s mark: '))
        if mark in range (0,101):
            total_marks.append(mark)

        else:
         print ('Please input correct mark.')
         raise SystemExit

    average_mark = sum(total_marks) / NUMBER_OF_MARKS

    print ('Final Mark for ' + name.capitalize() + ' is ' + str(average_mark))



except ValueError:
    print ('Enter a number, please')


