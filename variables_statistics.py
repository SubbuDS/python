import pandas as pd
wnba = pd.read_csv('wnba.csv')

variables = {'Name': '', 'Team': '', 'Pos': '', 'Height': '', 'BMI': '',
             'Birth_Place': '', 'Birthdate': '', 'Age': '', 'College': '', 'Experience': '',
             'Games Played': '', 'MIN': '', 'FGM': '', 'FGA': '',
             '3PA': '', 'FTM': '', 'FTA': '', 'FT%': '', 'OREB': '', 'DREB': '',
             'REB': '', 'AST': '', 'PTS': ''}
variables = {'Name': 'qualitative', 'Team': 'qualitative', 'Pos': 'qualitative',
             'Height': 'quantitative', 'BMI': 'quantitative',
             'Birth_Place': 'qualitative', 'Birthdate': 'quantitative', 'Age': 'quantitative', 
             'College': 'qualitative', 'Experience': 'quantitative', 'Games Played': 'quantitative',
             'MIN': 'quantitative', 'FGM': 'quantitative', 'FGA': 'quantitative',
             '3PA': 'quantitative', 'FTM': 'quantitative',
             'FTA': 'quantitative', 'FT%': 'quantitative', 'OREB': 'quantitative', 'DREB': 'quantitative',
             'REB': 'quantitative', 'AST': 'quantitative', 'PTS': 'quantitative'}
             
             
             
nominal_scale = sorted(['Name', 'Team', 'Pos', 'Birth_Place', 'College'])


question1 = True
question2 = False
question3 = False
question4 = True
question5 = False
question6 = False



interval = ['Birthdate', 'Weight_deviation']
ratio = sorted(['Height', 'Weight', 'BMI', 'Age', 'Experience', 'Games Played', 'MIN', 'FGM', 'FGA', 'FG%', '15:00', 
                '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TO',
                'PTS', 'DD2', 'TD3'])
                
                
                
