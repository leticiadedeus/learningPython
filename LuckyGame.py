import random
from operator import itemgetter
game = dict()
game['player 1'] = random.randint(0, 6)
game['player 2'] = random.randint(0, 6)
game['player 3'] = random.randint(0, 6)
game['player 4'] = random.randint(0, 6)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
for i, p in enumerate(ranking):
    print(f'{i+1}º = {p[0]} - with value {p[1]}')
