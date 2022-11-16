from ptcg_api.card_database import CardDatabase
import config
# from urllib.request import Request, urlopen
# from urllib.error import HTTPError

import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Select, Button

MY_GUILD = discord.Object(id=config.GUILD_ID)

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

intents = discord.Intents.default()
client = MyClient(intents=intents)
database = CardDatabase()


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.tree.command(
    name='lookup', 
    description='Get info on a Pokémon card', 
    guild=MY_GUILD
)
@app_commands.rename(card_name='card') # Shows "card" instead of "card_name"
@app_commands.describe(card_name='Name of the Pokémon card')
async def lookup(interaction: discord.Interaction, card_name: str):
    # Input card name through command parameter

    # Check for valid card name
    
    # Option: ask what set card is from suggested autofill of all valid set names when typing
    # Loop through all valid sets with card name
    # Skip button
    # skip = Button

        
    # Shows all results through embedded message

    # Load image
    # for card in cards:
        #     print(card.id)
        #     # print("Downloading " + card.name)
        #     # url = card.images.small
        #     # urllib.request.urlretrieve(url, card.id + ".png")

    # Find card using name and set
    # If multiple results, edit message to cycle through results via buttons
    
    # Added to watchlist button, or timeout message

    # Menu for lookup
    # embedVar = discord.Embed(title="Title", description="Desc", color=0xb08f81)
    # embedVar.add_field(name="Field1", value="hi", inline=False)
    # embedVar.add_field(name="Field2", value="hi2", inline=False)
    await interaction.response.send_message(card_name)

# Suggested autofill of all valid card names when typing
from typing import List
@lookup.autocomplete('card_name')
async def card_name_autocomplete(interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
    # choices = [
    #     app_commands.Choice(name=choice, value=choice)
    #     for choice in client.card_names if current.lower() in choice.lower()
    # ]    
    # return choices[:25] if (len(choices) > 25) else choices

    choices = []
    for choice in database.unique_names:
        if current.lower() in choice.lower():
            choices.append(app_commands.Choice(name=choice, value=choice))     
        if len(choices) == 25: break
    return choices

# @tree.command(name="remove", description="Remove card from watchlist", guild=discord.Object(id=GUILD_ID))
# async def self(interaction: discord.Interaction):
    # REMOVE
    # Input all Pokémon names you want to remove from watchlist, suggested autofill of all valid card names when typing

    # Click off, message embed with list of cards wanted to be removed
    # "Redo Cards" and "Confirm" buttons

# @tree.command(name="watchlist", description="View your watchlist", guild=discord.Object(id=GUILD_ID))
# async def self(interaction: discord.Interaction):
    # WATCHLIST
    # Menu with navigation buttons to view pages of watchlist
    # Dropdown to sort by presets

# @client.tree.command(name='ping', description='Get bot latency', guild=discord.Object(id=config.GUILD_ID))
# async def self(interaction: discord.Interaction):
#     await interaction.response.send_message(f'{round(client.latency * 1000)}ms', ephemeral=True)

client.run(config.TOKEN)