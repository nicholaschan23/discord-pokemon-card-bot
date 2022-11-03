import discord
from discord import app_commands
from discord.ext import commands

from config import *

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class test(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    
    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=SERVER_ID))
        self.synced = True
        print(f'{client.user} is now running.')

client = test()
tree = app_commands.CommandTree(client)

@tree.command(name="lookup", description="Search a Pokémon card on TCGPlayer", guild=discord.Object(id=SERVER_ID))
async def self(interaction: discord.Interaction, name: str):
    # Menu for lookup
    embedVar = discord.Embed(title="Title", description="Desc", color=0xb08f81)
    embedVar.add_field(name="Field1", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    # await interaction.channel.send(embed=embedVar)
    await interaction.channel.send(view=Menu())

@tree.command(name="ping", description="Bot latency", guild=discord.Object(id=SERVER_ID))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"{round(client.latency * 1000)}ms", ephemeral=True)

class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Send Message", style=discord.ButtonStyle.gray)
    async def menu1(self, button: discord.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Hello")
    
    @discord.ui.button(label="Edit Embed", style=discord.ButtonStyle.gray)
    async def menu2(self, button: discord.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="Edited", color=0xffffff)
        await interaction.response.edit_message(embed=embed)
        # self.value = False
        # self.stop()

def run():
    client.run(TOKEN)