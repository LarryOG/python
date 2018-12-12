Team_Name = input('Enter the Team Name: \n')
Number_of_Results = 5

goals_scored_in_games = []
goals_against_in_games = []
try:
    for count in range (Number_of_Results):
        goals_scored = int(input('Goals Scored in Match #'+ str(count + 1)+': '))
        goals_scored_in_games.append (goals_scored)
        goals_against = int(input('Goals Against in Match #'+ str(count + 1)+': '))
        goals_against_in_games.append (goals_against)
        wins = 0
        draws = 0
        loses = 0
        points = 0
except ValueError:
    print('Error. Enter an integer.')

for i in range (Number_of_Results):
    if goals_against_in_games[i] < goals_scored_in_games[i]:
     wins += 1
    elif goals_against_in_games[i] > goals_scored_in_games[i]:
     loses += 1
    elif goals_scored_in_games[i] == goals_against_in_games[i]:
     draws += 1
points = wins * 3 + draws
print(Team_Name.capitalize() + ': ','\nWins: ', wins,'\nDraws: ', draws,
      '\nLoses: ',loses,'\nPoints: ',points)

