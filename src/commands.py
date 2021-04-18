from config import credential
from discord.ext import commands
from handlers import team_controller, task_controller, audit_controller, view_controller

def start():

    help_command = commands.DefaultHelpCommand(no_category = 'dCTF')
    bot = commands.Bot(command_prefix='>>', help_command = help_command)

    @bot.command(name='register', help='Register your team. Format: >>register <team_name>')
    async def register(ctx, team: str):
        response = team_controller.register(team)
        await ctx.send(response)

    @bot.command(name='login', help='Login with team token. Format: >>login <team_token>')
    async def login(ctx, token: str):
        response = team_controller.login(str(ctx.author.id), token)
        await ctx.send(response)
    
    @bot.command(name='create-challenge', help='Format: >>create-challenge <name> <category> <description> <files> <flag>')
    @commands.has_role(credential.role)
    async def create_task(ctx, name: str, category: str, description: str, files: str, flag: str):
        response = task_controller.create_task(name, category, description, files, flag)
        await ctx.send(response)
    
    @bot.command(name='release-challenge', help='Format: >>release-challenge <challenge_id>')
    @commands.has_role(credential.role)
    async def release_task(ctx, task_id: int):
        response = task_controller.release_task(task_id)
        await ctx.send(response)

    @bot.command(name='hide-challenge', help='Hide a challenge. Format: >>hide-challenge <challenge_id>')
    @commands.has_role(credential.role)
    async def hide_task(ctx, task_id: int):
        response = task_controller.hide_task(task_id)
        await ctx.send(response)

    @bot.command(name='delete-challenge', help='Format: >>delete-challenge <challenge_id>')
    @commands.has_role(credential.role)
    async def delete_task(ctx, task_id: int):
        response = task_controller.delete_task(task_id)
        await ctx.send(response)
    
    @bot.command(name='submit', help='Submit flag. Format: >>submit <flag>')
    async def submit(ctx, flag: str):
        response = audit_controller.submit(str(ctx.author.id), flag)
        await ctx.send(response)

    @bot.command(name='challenges', help='List all challenges. Format: >>challenges')
    async def challenges(ctx):
        response = view_controller.challenges()
        await ctx.send(embed=response)

    @bot.command(name='challenges-info', help='Get challenges info. Format: >>chllenges-info <name>')
    async def challenges_info(ctx, name: str):
        response = view_controller.challenges_info(name)
        await ctx.send(embed=response)

    @bot.command(name='scoreboard', help='Update scoreboard. Format: >>scoreboard')
    async def scoreboard(ctx):
        response=view_controller.scoreboard_before_freeze()
        await ctx.send(response)

    bot.run(credential.token)
