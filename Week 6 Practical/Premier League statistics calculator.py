Team_Name = input('Enter the Team Name: \n')
Number_of_Results = 5

goals_scored_in_games = []
goals_against_in_games = []

for count in range (Number_of_Results):
    goals_scored = int(input('Goals Scored in Match #'+ str(count + 1)+': '))
    goals_scored_in_games.append (goals_scored)
    goals_against = int(input('Goals Against in Match #'+ str(count + 1)+': '))
    goals_against_in_games.append (goals_against)

