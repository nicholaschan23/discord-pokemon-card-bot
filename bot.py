import discord
from discord import app_commands
from discord.ext import commands

from config import TOKEN, SERVER_ID

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

@tree.command(name="ping", description="Bot latency", guild=discord.Object(id=SERVER_ID))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"{round(client.latency * 1000)}ms", ephemeral=True)

def run():
    client.run(TOKEN)