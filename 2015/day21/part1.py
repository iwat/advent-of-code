from itertools import product


weapons = {
    'Dagger': {'cost': 8, 'dmg': 4, 'armor': 0},
    'Shortsword': {'cost': 10, 'dmg': 5, 'armor': 0},
    'Warhammer': {'cost': 25, 'dmg': 6, 'armor': 0},
    'Longsword': {'cost': 40, 'dmg': 7, 'armor': 0},
    'Greataxe': {'cost': 74, 'dmg': 8, 'armor': 0},
}

armors = {
    'Bare': {'cost': 0, 'dmg': 0, 'armor': 0},
    'Leather': {'cost': 13, 'dmg': 0, 'armor': 1},
    'Chainmail': {'cost': 31, 'dmg': 0, 'armor': 2},
    'Splintmail': {'cost': 53, 'dmg': 0, 'armor': 3},
    'Bandedmail': {'cost': 75, 'dmg': 0, 'armor': 4},
    'Platemail': {'cost': 102, 'dmg': 0, 'armor': 5},
}

rings = {
    'NoRing1': {'cost': 0, 'dmg': 0, 'armor': 0},
    'NoRing2': {'cost': 0, 'dmg': 0, 'armor': 0},
    'Damage +1': {'cost': 25, 'dmg': 1, 'armor': 0},
    'Damage +2': {'cost': 50, 'dmg': 2, 'armor': 0},
    'Damage +3': {'cost': 100, 'dmg': 3, 'armor': 0},
    'Defense +1': {'cost': 20, 'dmg': 0, 'armor': 1},
    'Defense +2': {'cost': 40, 'dmg': 0, 'armor': 2},
    'Defense +3': {'cost': 80, 'dmg': 0, 'armor': 3},
}


def best_fight(boss_hp, boss_dmg, boss_armor):
    best_win = None
    best_combination = None
    for comb in product(weapons.items(), armors.items(), rings.items(), rings.items()):
        if comb[2] == comb[3]:
            continue

        player_hp = 100
        player_dmg = sum([props['dmg'] for name, props in comb])
        player_armor = sum([props['armor'] for name, props in comb])
        cost = sum([props['cost'] for name, props in comb])

        winner = fight(player_hp, player_dmg, player_armor, boss_hp, boss_dmg, boss_armor)

        if winner == 'Player':
            if best_win is None or cost < best_win:
                best_win = cost
                best_combination = tuple([name for name, _ in comb])
                print(best_combination, best_win, player_hp, player_dmg, player_armor)

    return (best_combination, best_win)

def fight(player_hp, player_dmg, player_armor, boss_hp, boss_dmg, boss_armor):
    turn = 0
    while player_hp > 0 and boss_hp > 0:
        if turn == 0:
            boss_hp -= max(1, player_dmg - boss_armor)
        else:
            player_hp -= max(1, boss_dmg - player_armor)
        turn = (turn + 1) % 2
    if player_hp > 0:
        return 'Player'
    return 'Boss'


if __name__ == '__main__':
    print(best_fight(boss_hp=109, boss_dmg=8, boss_armor=2))