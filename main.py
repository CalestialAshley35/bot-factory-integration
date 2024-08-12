import discord
from discord.ext import commands
from googleapiclient.discovery import build

# Your YouTube Data API key
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'

# Initialize the YouTube API client
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

# Create a new bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def search(ctx, *, query):
    try:
        # Search YouTube for the query
        request = youtube.search().list(
            part='snippet',
            q=query,
            type='video',
            maxResults=1
        )
        response = request.execute()

        if response['items']:
            video = response['items'][0]
            video_id = video['id']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            await ctx.send(f'Here is the video link: {video_url}')
        else:
            await ctx.send('No results found.')

      except Exception as e:
          await ctx.send(f'An error occurred: {e}')

# Replace 'YOUR_BOT_TOKEN' with your Discord bot token
bot.run('YOUR_BOT_TOKEN')