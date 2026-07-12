#welcome to my code, the library
import random
from colorama import Fore, Style

colors_list = [
    Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.RED,
    Fore.LIGHTRED_EX, Fore.LIGHTMAGENTA_EX, Fore.MAGENTA
]

Games = {}
Games['name'] = ['']
Games['publisher'] = ["Hoyoverse", "Warner Bros", "Lucasfilm", "Ubisoft", "Blizzard", "XBox"]
Games['genre'] = ['Fighting', 'Fantasy', 'Puzzle', "Meta", "Racing"]
Games['year'] = ['2015', '2016', '2017', '2018', '2013', '2022', '2024']
Games['price'] = ['1k', '1.5k', '2k', '3k', '4k', '5k']
gspecs = [ 'publisher', 'genre', 'year', 'price']

Books = {}
Merchandise = {}
Books["name"] = []
Books["publisher"] = ['Bloomsbury', 'Scholastic', 'crossword', 'PuffinBooks', 'Penguin']
Books["genre"] = ["Fantasy", 'action', 'romance', 'motivation', 'guide', 'other']
Books['pageno'] = ['150', '250', '350', '400', '580', '600', '800', 'more']
Books['price'] = ['500INR', '700INR', '900', '1000', '1500', '2000']
specs = ['publisher', 'genre', 'pageno', 'price']

n_books = 40
numberlist = [number for number in range(40)]
booklist = []
for _ in range(n_books):
    newbook = {spec: random.choice(Books[spec]) for spec in specs}
    newbook['name'] = ['Book' + str(random.choice(numberlist))]
    booklist.append(newbook)

n_games = 40
numberlist = [number for number in range(40)]
gamelist = []
for _ in range(n_games):
    newgame = {gspec: random.choice(Games[gspec]) for gspec in gspecs}
    newgame['name'] = ['Game' + str(random.choice(numberlist))]
    gamelist.append(newgame)


def matches_preferences(item, conditions):
    return all(item.get(key) == value for key, value in conditions)


libwhich = input("would you like to see our game library or book library, type game for game and book for well you get it")

if libwhich == 'book':
    user_choice = dict.fromkeys(specs)
    for kk in specs:
        print(Books[kk])
        user_choice[kk] = input('any preferences for ' + kk + ' enter none for no preference' + '\n')

    conditions = []
    for kk in user_choice:
        preference = user_choice[kk]
        if preference.lower() != 'none':
            conditions.append((kk, preference))

    selected = [book for book in booklist if matches_preferences(book, conditions)] if conditions else list(booklist)

    for book in selected:
        color = random.choice(colors_list)
        print(color + str(book) )
    if not selected:
        print("We have failed our purose, here is a free Shonen Book box, the full set, and a Rick Riordan book box")
    

if libwhich == 'game':
    user_choice2 = dict.fromkeys(gspecs)
    for kk in gspecs:
        print(Games[kk])
        user_choice2[kk] = input('any preferences for ' + kk + ' enter none for no preference' + '\n')

    conditions2 = []
    for kk in user_choice2:
        if user_choice2[kk].lower() != 'none':
            conditions2.append((kk, user_choice2[kk]))

    selected = [game for game in gamelist if matches_preferences(game, conditions2)] if conditions2 else list(gamelist)

    for game in selected:
        color = random.choice(colors_list)
        print(color + str(game) )
    if not selected:
        print("We have failed our purose, here is a free copy of genshin impact, and hogwarts legacy")