player = dict()
player['name'] = str(input('Name of the player: '))
player['games'] = int(input(f'How many games did {player["name"]} play? '))
player['goals'] = list()
player['totalGoals'] = 0
for c in range(0, player['games']):
    g = (int(input(f' - How many goals they did on the {c + 1} game? ')))
    player['goals'].append(g)
    player['totalGoals'] = player['totalGoals'] + g
# for k, v in player.items():
#     print(f'{k} -> {v}')
print('-=' * 30)
for k, v in enumerate(player['goals']):
    print(f'On the game {k + 1}, {player["name"]} made {v} goals')
print(f'total goals = {player["totalGoals"]}')
