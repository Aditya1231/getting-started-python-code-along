# --------------
import yaml

# Read the data of the format .yaml type
#f = open(path) #reading 
#data = yaml.load(f)
#print(data)
with open(path) as f:
    data = yaml.load(f)

#print(data)
# Find data type of the file
type_of_data = type(data)
print('data type of file is  after reading',type_of_data)
# In which city, and at which venue the match was played and where was it played ?
match_info = data['info']
match_city = match_info['city']
print('Match city',match_city)


# Which are all the teams that played in the tournament ? How many teams participated in total?
team_playing = data['info']['teams']
print('Teams playing',team_playing[0],'and',team_playing[1])

print('Total number of teams playing',len(team_playing))

# Which team won the toss and what was the decision of toss winner ?
#data['info'].keys()
toss = data['info']['toss']['winner']
decision = data['info']['toss']['decision']
print('Team won the toss',toss,'Decision taken ',decision)

# Find the first bowler and first batsman who played the first ball of the first inning
batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']

print('First Batsman:', batsman)
print('First Bowler:', bowler)

# How many deliveries were delivered in first inning ?
first_len_deliveries = len(data['innings'][0]['1st innings']['deliveries'])
print('First innings deliveries',first_len_deliveries)

# How many deliveries were delivered in second inning ?
second_len_deliveries = len(data['innings'][1]['2nd innings']['deliveries'])
print('Second Innings deliveries', second_len_deliveries)

# Which team won and how ?
runs = data['info']['outcome']['by']['runs']
winning_team = data['info']['outcome']['winner']
print('Winning Team ',winning_team,'they won by "'+ str(runs)+ "\" runs")


