import csv
import random
from pathlib import Path

import pyfiglet

ATTRIBUTE_CHOICES = {
    'M': 'Magic',
    'C': 'Cunning',
    'CO': 'Courage',
    'W': 'Wisdom',
    'T': 'Temper',
}


def display(card):
    maxchars = max(len(key) for key in card)
    for key in card:
        print(key, ' ' * (maxchars - len(key)), ' : ', card[key])


def determine(m1, m2, order=1):
    dct = {'player': m1, 'computer': m2}
    values = list(dct.values())
    names = list(dct.keys())
    if m1 == m2:
        print('Draw')
        return None

    if order == 1:
        return names[values.index(max(values))]
    else:
        return names[values.index(min(values))]


def normalise_attribute(choice, mapping):
    if not choice:
        return None

    normalised = choice.strip().upper()
    if normalised in mapping:
        return normalised

    for short_code, attribute_name in mapping.items():
        if normalised == attribute_name.upper():
            return short_code

    return None


def choose_attribute(mapping, is_player_turn, prompt='Which attribute do you wish to compare [M,C,CO,W,T]: '):
    if is_player_turn:
        while True:
            chosen = input(prompt).strip()
            normalised = normalise_attribute(chosen, mapping)
            if normalised:
                return normalised
            print('Please choose a valid attribute.')

    return random.choice(list(mapping.keys()))


def main():
    csv_path = Path(__file__).with_name('Top Trumps - Harry Potter and the Deathly Hallows Part 2.csv')
    with csv_path.open(mode='r', newline='') as file:
        allcards = list(csv.DictReader(file))

    if not allcards:
        raise ValueError('No cards were found in the CSV file.')

    available_attributes = [key for key in allcards[0].keys() if key != 'Individual']
    mappingdict = {}
    for short_code, attribute_name in ATTRIBUTE_CHOICES.items():
        if attribute_name in available_attributes:
            mappingdict[short_code] = attribute_name

    if not mappingdict:
        raise ValueError('No supported attributes were found in the CSV file.')
    
    

    random.shuffle(allcards)
    computercards = allcards[::2]
    pcards = allcards[1::2]
    tablecards = []
    gameover = False
    chance = 'player'

    while not gameover:
        print('player cards:', len(pcards), '\n', 'computer cards:', len(computercards), '\n', 'table cards:', tablecards)

        if not pcards or not computercards:
            break

        player = pcards.pop(0)
        com = computercards.pop(0)

        tablecards.append(player)
        tablecards.append(com)

        print()
        print('your card is  :')
        display(player)

        if chance == 'player':
            chosenkey = choose_attribute(mappingdict, True)
            chance = 'computer'
        else:
            chosenkey = choose_attribute(mappingdict, False)
            chance = 'player'

        keyreq = mappingdict[chosenkey]
        valuep = int(player[keyreq])
        valueq = int(com[keyreq])

        print('key of interest is:', keyreq)

        if chosenkey in ['M', 'C', 'CO', 'W']:
            winner = determine(valuep, valueq)
        else:
            winner = determine(valuep, valueq, 0)

        print('player value is', valuep)
        print('computer value is', valueq)
        print('winner is ', winner)

        if winner == 'player':
            pcards.extend(tablecards)
            tablecards.clear()
        elif winner == 'computer':
            computercards.extend(tablecards)
            tablecards.clear()
        else:
            # tie/draw: leave tablecards on the table for the next round
            print('Round is a draw — cards remain on the table')

        if len(pcards) == 0:
            print(pyfiglet.figlet_format('WInner is Player', font='gothic'))
            gameover = True
        elif len(computercards) == 0:
            print(pyfiglet.figlet_format('WInner is Computer', font='gothic'))
            gameover = True


if __name__ == '__main__':
    main()
