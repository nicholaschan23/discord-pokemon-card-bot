import config
import os
import pickle
from urllib.request import Request, urlopen
from urllib.error import HTTPError

import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Select

from pokemontcgsdk import RestClient, Card, Set, Rarity

class DiscordBot(discord.Client):
    # Set of all unqiue card names
    card_names = []

    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

        RestClient.configure(config.POKEMONTCG_IO_API_KEY)
        self.fetch_card_names()
        # self.fetch_sets()
    
    async def on_ready(self):
        if (not self.synced):
            # Instantenous guild-specific syncing
            await tree.sync(guild=discord.Object(id=config.SERVER_ID))
            self.synced = True # Sync commands once
        print(f'{client.user} is now running.')

    # Pre-processing all card names
    def fetch_card_names(self):
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

        self.card_names = set([card.name for card in cards])
        print(f'Processed {len(self.card_names)} unique card names')
    
client = DiscordBot()
# Container for all slash commands
tree = app_commands.CommandTree(client)

@tree.command(name='lookup', description='Find a Pokémon card', guild=discord.Object(id=config.SERVER_ID))
async def lookup(interaction: discord.Interaction, card_name: str):
    # LOOKUP
    # Input name from command parameter, suggested autofill of all valid card names when typing


    # Option: ask what set card is from suggested autofill of all valid set names when typing
    # Loop through all valid sets with card name
    # Skip button
    
    # Shows all results through embedded message

    # Load image
    # for card in cards:
        #     print(card.id)
        #     # print("Downloading " + card.name)
        #     # url = card.images.small
        #     # urllib.request.urlretrieve(url, card.id + ".png")

    # If multiple results, edit message to cycle through results via buttons
    
    # Added to watchlist button, or timeout message

    # Menu for lookup
    # embedVar = discord.Embed(title="Title", description="Desc", color=0xb08f81)
    # embedVar.add_field(name="Field1", value="hi", inline=False)
    # embedVar.add_field(name="Field2", value="hi2", inline=False)
    # await interaction.channel.send(embed=embedVar)

    await interaction.response.send_message(f'{len(client.card_names)}')

from typing import List
@lookup.autocomplete('card_name')
async def card_name_autocomplete(interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
    # choices = [
    #     app_commands.Choice(name=choice, value=choice)
    #     for choice in client.card_names if current.lower() in choice.lower()
    # ]    
    # return choices[:25] if (len(choices) > 25) else choices

    choices = []
    for choice in client.card_names:
        if len(choices) == 25: break
        if current.lower() in choice.lower():
            choices.append(app_commands.Choice(name=choice, value=choice))     
    return choices

# @tree.command(name="remove", description="Remove card from watchlist", guild=discord.Object(id=SERVER_ID))
# async def self(interaction: discord.Interaction):
    # REMOVE
    # Input all Pokémon names you want to remove from watchlist, suggested autofill of all valid card names when typing

    # Click off, message embed with list of cards wanted to be removed
    # "Redo Cards" and "Confirm" buttons

# @tree.command(name="watchlist", description="View your watchlist", guild=discord.Object(id=SERVER_ID))
# async def self(interaction: discord.Interaction):
    # WATCHLIST
    # Menu with navigation buttons to view pages of watchlist
    # Dropdown to sort by presets

@tree.command(name='ping', description='Get bot latency', guild=discord.Object(id=config.SERVER_ID))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f'{round(client.latency * 1000)}ms', ephemeral=True)

# class CardEmbed(discord.ui.View):
#     def __init__(self):
#         super().__init__()
#         self.value = None

#     @discord.ui.button(label="Send Message", style=discord.ButtonStyle.gray)
#     async def menu1(self, button: discord.Button, interaction: discord.Interaction):
#         await interaction.response.send_message("Hello")
    
#     @discord.ui.button(label="Edit Embed", style=discord.ButtonStyle.gray)
#     async def menu2(self, button: discord.Button, interaction: discord.Interaction):
#         embed = discord.Embed(title="Edited", color=0xffffff)
#         await interaction.response.edit_message(embed=embed)
#         # self.value = False
#         # self.stop()

def run():
    client.run(config.TOKEN)