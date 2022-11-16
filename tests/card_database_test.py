import random
import sys
sys.path.append('..')

from ptcg_api.card_database import CardDatabase

def main():
    data = CardDatabase()
    print('Lengths should be the same')
    print(f'UNIQUE NAMES: {len(data.unique_names)}')
    print(f'SET MATCHING: {len(data.unique_names)}')

    # Picks a random card and prints the sets its in
    i = random(0, len(data.unique_names))
    for j in data.set_matching[data.unique_names[i]]:
        print(data.set_matching[data.unique_names[i][j]])
    print(f'{data.unique_names[i]} is in {len(data.set_matching[data.unique_names[i]])} set(s)')
    print('------')

if __name__ == "__main__":
    main()