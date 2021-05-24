import os
import overview_recommend
from discord.ext import commands

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

# Command to find recommended movie based on overview of the movies
@bot.command()
async def recommend_title(ctx, *args):
	movie_name = ' '.join(args)
	print(movie_name)
	print(f"User: {ctx.author.name}\nGuild: {ctx.guild}\nMovie: {movie_name}\nType: Title")
	
	# Writing logs of the tasks performed
	with open("logs.txt","a") as logs:
		logs.write(f"User: {ctx.author.name}\nGuild: {ctx.guild}\nMovie: {movie_name}\nType: Title")
	
	try:
		recommended_movies = overview_recommend.give_only_title(' '.join([i.capitalize() for i in args]))
	except:
		recommended_movies = overview_recommend.give_only_title(movie_name)
	
	print('\n'.join(recommended_movies))
	await ctx.send('\n'.join(recommended_movies))

# Command to find recommended movie based on overview of the movies as well as score
@bot.command()
async def recommend_title_score(ctx, *args):
	movie_name = ' '.join(args)
	print(movie_name)
	print(f"User: {ctx.author.name}\nGuild: {ctx.guild}\nMovie: {movie_name}\nType:Title_Score")
	with open("logs.txt","a") as logs:
		logs.write(f"User: {ctx.author.name}\nGuild: {ctx.guild}\nMovie: {movie_name}\nType: Title_Score")
	try:
		recommended_movies = overview_recommend.give_title_score(' '.join([i.capitalize() for i in args]))
	except:
		recommended_movies = overview_recommend.give_title_score(movie_name)
	print('\n'.join(recommended_movies))
	await ctx.send('\n'.join(recommended_movies))

# Running the discord bot
token = os.environ["DISCORD_BOT_SECRET"]
bot.run(token)
