

a = float(input('Input 1st meter reading: '))
b = float(input('Input 2nd meter reading: '))
c = float(input('Input 3rd meter reading: '))
d = float(input('Input 4th meter reading: '))

temp_readings = [a,b,c,d]
average = (a+b+c+d)/4
print('Highest temperature:',max(temp_readings),'\nLowest temperature:',min(temp_readings),'\nTemperatures average: ',average)