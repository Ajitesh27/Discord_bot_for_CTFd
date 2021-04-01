import discord
from discord.ext import commands, tasks
from discord.ext.tasks import loop
from asyncio import sleep
from datetime import datetime, timedelta
import pytz
import backend

'''
https://discord.com/oauth2/authorize?client_id=770721845896019988&scope=bot&permissions=268435496
'''

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.
bot = commands.Bot(command_prefix='>', intents=intents)
bot.remove_command('help')


def authorized(username):
    with open('auth_user.txt') as user_list:
        if username in user_list.read():
            return True
        return False


@tasks.loop(minutes=30)
async def get_firstblood():
    print("firstblood")
    UTC = pytz.utc 
    timeZ_Kl = pytz.timezone('Asia/Kolkata')
    event_start = datetime(2020, 11, 6, 18, 30, 0).astimezone(timeZ_Kl)
    event_end = datetime(2020, 11, 8, 18, 0, 0).astimezone(timeZ_Kl)
    current_time = datetime.now().astimezone(timeZ_Kl)
    if current_time >= event_start and current_time <= event_end:
        channel = bot.get_channel(767645511121109003)
        message = backend.firstblood()
        if message != "NULL":
            await channel.send(message)
        else:
            pass
    if current_time > event_end:
        return 0


@tasks.loop(hours=1)
async def ctf_backup():
    print("backup")
    UTC = pytz.utc 
    timeZ_Kl = pytz.timezone('Asia/Kolkata')
    event_start = datetime(2020, 11, 6, 17, 30, 0).astimezone(timeZ_Kl)
    event_end = datetime(2020, 11, 8, 18, 0, 0).astimezone(timeZ_Kl)
    current_time = datetime.now().astimezone(timeZ_Kl)
    if current_time >= event_start and current_time <= event_end:
        backend.backup()
    if current_time > event_end:
        return 0


@tasks.loop()
async def random_message():
    print("random")
    UTC = pytz.utc 
    timeZ_Kl = pytz.timezone('Asia/Kolkata')    
    event_start = datetime(2020, 11, 6, 18, 0, 0).astimezone(timeZ_Kl)
    event_halfway = datetime(2020, 11, 7, 18, 0, 0).astimezone(timeZ_Kl)
    event_nearend = datetime(2020, 11, 8, 17, 0, 0).astimezone(timeZ_Kl)
    event_end = datetime(2020, 11, 8, 18, 0, 0).astimezone(timeZ_Kl)
    current_time = datetime.now().astimezone(timeZ_Kl)
    if current_time >= event_end and current_time < event_end + timedelta(minutes = 1):
        channel = bot.get_channel(767645511121109003)
        await channel.send("@Participant \nThe CTF has ended. Thank you all for participating")
        await sleep(60)
    elif current_time >= event_nearend and current_time < event_nearend + timedelta(minutes = 1):
        channel = bot.get_channel(767645511121109003)
        await channel.send("@Participant \nOnly 1 more hour until the CTF ends")
        await sleep(60)
    elif current_time >= event_halfway and current_time < event_halfway + timedelta(minutes = 1):
        channel = bot.get_channel(767645511121109003)
        await channel.send("@Participant \nIt's been 24 hours since the start. We have 24 more hours to go. Keep up the hacking.")
        await sleep(60)
    elif current_time >= event_start and current_time < event_start + timedelta(minutes = 1):
        channel = bot.get_channel(767645511121109003)
        await channel.send("@Participant \nHere is the link to the CTF. All the best.\nhttp://52.230.99.155/")
        await sleep(60)


@bot.event
async def on_ready():
    print("Bot is up and running")


@bot.event
async def on_message(message):
    print("[+] Msg -> ", message.content)
    await bot.process_commands(message)


@bot.command()
async def all_members(ctx):
    if authorized(ctx.author.name):
        for member in ctx.guild.members:
            if member.bot:
                continue
            else:
                await ctx.send(str(member).split('#')[0])
    else:
        await ctx.send("You're not authorized to speak to the bot")


@bot.command()
async def auth(ctx, *, username: str):
    if authorized(ctx.author.name):
        flag = False
        for member in ctx.guild.members:
            if str(member).split('#')[0] == username:
                flag = True
                with open("auth_user.txt", "r") as user_list_read:
                    if username in user_list_read.read():
                        await ctx.send(f"{username} is already authorized")
                    else:
                        with open("auth_user.txt", "a") as user_list_write:
                            user_list_write.write(f"{username}\n")
                            await ctx.send(f"{username} is authorized")
        if not flag:
            await ctx.send(f"{username} is not present on the server")
    else:
        await ctx.send("You're not authorized to speak to the bot")


@bot.command()
async def register(ctx, *, info: str):
    if authorized(ctx.author.name):
        flag = False
        username = info.split(' ')[0]
        mail = info.split(' ')[1]
        for member in ctx.guild.members:
            if str(member).split('#')[0] == username:
                flag = True
                if backend.register(username, mail):
                    await ctx.send(f"{username} has been registered. Credentials are sent to {mail}")
                else:
                    await ctx.send("The email doesn't work")
        if not flag:
            await ctx.send(f"{username} is not present on the server")
    else:
        await ctx.send("You're not authorized to speak to the bot")


@bot.command()
async def register_all(ctx):
    if ctx.author.name == 'AidynSkullz':
        member_list = []
        for member in ctx.guild.members:
            if member.bot:
                continue
            else:
                member_list.append(str(member).split('#')[0])
        await ctx.send("Registering all @Participant to the CTF")
        backend.register_all(member_list)
        await ctx.send("@Participant You all have been registered on the CTF platform. Login credentials are sent to your email. If you don't find it, check your spam folder.\nThe link to the CTF will be provided at 6:00 PM sharp.")
    else:
        await ctx.send("You're not authorized to run this command, even if you are authorized to run others")


@bot.command()
async def help(ctx):
    if authorized(ctx.author.name):
        message = '''**CTF Bot Commands**```
        >auth <user>                   Authorize a person to use the bot. Can only be done by someone already authorized
        >all_members                   Show list of all members on the server
        >register <user> <email>       Register a user to the CTF
        >register_all                  Register all participants to the CTF
        >help                          Show this message```'''
        await ctx.send(message)
    else:
        await ctx.send("You're not authorized to speak to the bot")


get_firstblood.start()
ctf_backup.start()
random_message.start()

TOKEN = "NzcwNzIxODQ1ODk2MDE5OTg4.X5hspw.8eAvTdDRQXdJU0IxdHlLXzWq0v0"
bot.run(TOKEN)  # Bot token
