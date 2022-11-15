import config
import os
import pickle
from collections import defaultdict

from pokemontcgsdk import RestClient, Card, Set, Rarity
RestClient.configure(config.POKEMONTCG_IO_API_KEY)

class CardDatabase:
    # Set of all unqiue card names
    unique_names = []
    # List of sets each unique card name is in
    card_to_set = defaultdict(list)

    def __init__(self):
        self.fetch()

    def fetch(self):
        cards = [] # Card object
        if os.path.isfile('cards.bin'):
            # Load cards from cached binary file if they exist
            with open('cards.bin', 'rb') as f:
                cards = pickle.load(f)
        else:
            # Get cards from the API if the cache file is missing
            cards = Card.all()
            with open('card.bin', 'wb') as f:
                # Store the cards
                pickle.dump(cards, f)
        print(f'Processed {len(cards)} cards')

        # Pre-process all card names
        self.unique_names = set([card.name for card in cards])
        print(f'Processed {len(self.unique_names)} unique card names')

        # Pre-process all sets card is in
        for card in cards:
            if card.set not in self.card_to_set[card.name]:
                self.card_to_set[card.name].append(card.set)
        print(f'Processed all sets card is in')