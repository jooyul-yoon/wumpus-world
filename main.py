import random


def rand_loc():
    x, y = int(random.random()*SIZE), int(random.random()*SIZE)
    while (x, y) in [(0, 0), (0, 1), (1, 0)]:
        x, y = int(random.random()*SIZE), int(random.random()*SIZE)
    return x, y


def generate_golds():
    count = 0
    while count < NUM_GOLDS:
        x, y = rand_loc()
        if set(map[x][y]['element']) & {'G', 'W', 'P'}:
            continue
        map[x][y]['element'] = 'G'
        count += 1


def generate_wumpus():
    count = 0
    while count < NUM_WUMPUS:
        x, y = rand_loc()
        if set(map[x][y]['element']) & {'G', 'W', 'P'}:
            continue
        map[x][y]['element'] = 'W'
        count += 1


def generate_pits():
    count = 0
    while count < NUM_PITS:
        x, y = rand_loc()
        if set(map[x][y]['element']) & {'G', 'W', 'P'}:
            continue
        map[x][y]['element'] = 'P'
        count += 1


def generate_env():
    for i in range(SIZE):
        for j in range(SIZE):
            elem = map[i][j]['element']
            if elem == 'P':
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + dx < SIZE and 0 <= j + dy < SIZE:
                        map[i + dx][j + dy]['env'].add('b')
            elif elem == 'G':
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + dx < SIZE and 0 <= j + dy < SIZE:
                        map[i + dx][j + dy]['env'].add('g')
            elif elem == 'W':
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + dx < SIZE and 0 <= j + dy < SIZE:
                        map[i + dx][j + dy]['env'].add('s')


def rng_map():
    generate_golds()
    generate_wumpus()
    generate_pits()
    generate_env()
    print_table(map)


def print_table(map):
    row_length = len(map)
    col_length = len(map[0]) if row_length > 0 else 0

    max_lengths = [5] * SIZE

    print('┌' + '─' * (sum(max_lengths) + col_length - 1) + '┐')

    for i, row in enumerate(map):
        print('│' + '│'.join(('  '+row[i]['element']).ljust(
            max_lengths[i]) for i in range(col_length)) + '│')
        print('│' + '│'.join((' '.join(list(row[i]['env']))).ljust(
            max_lengths[i]) for i in range(col_length)) + '│')
        if i != SIZE - 1:
            print('|' + '|'.join(['─' * 5] * SIZE) + '|')

    print('└' + '─' * (sum(max_lengths) + col_length - 1) + '┘')


SIZE = 4
NUM_GOLDS = 1
NUM_WUMPUS = 1
NUM_PITS = 4

map = [[{'element': '', 'env': set()}
        for _ in range(SIZE)] for _ in range(SIZE)]

rng_map()
