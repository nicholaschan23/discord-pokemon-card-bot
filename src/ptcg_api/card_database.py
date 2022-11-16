from config import *
import os
import pickle
from collections import defaultdict

from pokemontcgsdk import RestClient, Card, Set, Rarity
RestClient.configure(POKEMONTCG_IO_API_KEY)

class CardDatabase:
    def __init__(self):
        # Set of all unqiue card names
        self.unique_names = []
        # List of sets each unique card name is in
        self.set_matching = defaultdict(list)
        # Set of card ids
        self.card_ids = []

        self.__fetch__()

    def __fetch__(self):
        print(f'Starting preprocesses...')
        
        # Preprocess all cards
        cards = [] # Card object
        if os.path.isfile(f'{CARDS}.bin'):
            # Load cards from cached binary file if they exist
            print(f'{CARDS} cache file found')
            with open(f'{CARDS}.bin', 'rb') as f:
                cards = pickle.load(f)
        else:
            # Get cards from the API if the cache file is missing
            print(f'{CARDS} cache file not found. Sourcing from API')
            # cards = Card.all()
            cards = Card.where(q='name:"*"')
            with open(f'{CARDS}.bin', 'wb') as f:
                # Store the cards
                pickle.dump(cards, f)
        print(f'Processed {len(cards)} cards')


        # Preprocess all unique card names
        if os.path.isfile(f'{UNIQUE_NAMES}.bin'):
            print(f'{UNIQUE_NAMES} cache file found')
            with open(f'{UNIQUE_NAMES}.bin', 'rb') as f:
                self.unique_names = pickle.load(f)
        else:
            print(f'{UNIQUE_NAMES} cache file not found. Sourcing from API')
            self.unique_names = set([card.name for card in cards])
            with open(f'{UNIQUE_NAMES}.bin', 'wb') as f:
                pickle.dump(self.unique_names, f)
        print(f'Processed {len(self.unique_names)} unique card names')


        # Preprocess all card to set matching
        if os.path.isfile(f'{SET_MATCHING}.bin'):
            print(f'{SET_MATCHING} cache file found')
            with open(f'{SET_MATCHING}.bin', 'rb') as f:
                self.set_matching = pickle.load(f)
        else:
            print(f'{SET_MATCHING} cache file not found. Sourcing from API')
            for card in cards:
                if card.set not in self.set_matching[card.name]:
                    self.set_matching[card.name].append(card.set)
            with open(f'{SET_MATCHING}.bin', 'wb') as f:
                pickle.dump(self.set_matching, f)
        print(f'Processed all sets each unique card name is in')
        
        # Preprocess all card ids
        if os.path.isfile(f'{CARD_IDS}.bin'):
            print(f'{CARD_IDS} cache file found')
            with open(f'{CARD_IDS}.bin', 'rb') as f:
                self.card_ids = pickle.load(f)
        else:
            print(f'{CARD_IDS} cache file not found. Sourcing from API')
            self.card_ids = set([card.id for card in cards])
            with open(f'{CARD_IDS}.bin', 'wb') as f:
                pickle.dump(self.CARD_IDS, f)
        print(f'Processed all card ids')
        print('------')