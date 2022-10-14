import discord
from discord.ext import commands
import json
import asyncio

configs = None

try:
    with open("configs.json", "r", encoding="utf-8") as f:
        configs = json.load(f)
except Exception as e:
    print(e)
    print("Can\'t read config file.")


intents = discord.Intents().default()
intents.members = True

bot = discord.Bot(
    intents=intents,
    owner_id=configs.OWNER_ID,
    activity=discord.Activity(type=discord.ActivityType.watching, name="Server"),
    status=discord.Status.online,
)

@bot.event
async def on_ready() -> None:
    ''' the bot is ready'''
    print(f"The bot is connected: {bot.user}")


update = bot.create_group(name="update", description="Update server role.")
reload = bot.create_group(name="reload", description="Reload the add and del role lists")

@update.command(name = "roles", help = "This command can update role(s) of the server members.")
@commands.is_owner()
async def update_roles(ctx: discord.ApplicationContext) -> None:
    ''' This command can update role(s) of the server members. '''
    global white_list

    embed = discord.Embed(
        title="Role Manager", 
        description="Started to update roles.", 
        color=discord.Colour.from_rgb(222, 199, 241)
    )
    embed.set_author(
        name="0xmimiQ",
        url="https://twitter.com/0xmimiQ",
        icon_url="https://i.imgur.com/TSIudVh.png"
    )

    await ctx.respond(embed=embed, ephemeral=False)

    guild = ctx.author.guild
    add_role_list = []
    del_role_list = []

    for id in configs.ADD_ROLE_ID:
        role = discord.utils.get(guild.roles, id=id)
        add_role_list.append(role)
    
    for id in configs.DEL_ROLE_ID:
        role = discord.utils.get(guild.roles, id=id)
        del_role_list.append(role)

    for member in guild.members:
        for role in add_role_list:
            try:
                await member.add_roles(role)
            except Exception as e:
                print(e)
                print(f"When add role: {member.name}, something went wrong!")
            finally:
                await asyncio.sleep(0.2) # Discord API limit

        for role in del_role_list:
            try:
                await member.remove_roles(role)
            except Exception as e:
                print(e)
                print(f"When delete role: {member.name}, something went wrong!")
            finally:
                await asyncio.sleep(0.2) # Discord API limit

    await ctx.respond("End the update.")


@reload.command(name = "lists", help = "This command reloads the lists of role(s) to update.")
@commands.is_owner()
async def reload_lists(ctx: discord.ApplicationContext) -> None:
    try:
        with open("configs.json", "r", encoding="utf-8") as f:
            configs.clear()
            configs = json.load(f)
    except Exception as e:
        print(e)
        await ctx.respond("Can\'t read config file.")

    await ctx.respond("The lists have been reloaded.")

bot.run(configs.BOT_TOKEN)