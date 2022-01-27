import discord
from discord.ext import commands

#prefix za bota
client = commands.Bot(command_prefix=">")

#Pokretanje Bota
@client.event
async def on_ready():
    print("[+] Bot je pokrenut.")

@client.command()
async def test(ctx):
    embed = discord.Embed(
        colour = discord.Colour.purple()
    )

    embed.add_field(name = ":fire: UPSIDE" , value = "***UPSIDE - DEVELOPING***")
    await ctx.send(embed = embed)

#Komanda za Bota
@client.command()
async def hello(ctx):
    await ctx.send("Zdravo")

client.run("VAS DISKORD TOKEN")
