import os
import dotenv
from twitchio.ext import commands
import obsws_python as obs
import playsound

dotenv.load_dotenv()

allowed_users = []

# set up the bot
bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

def do_magic():
    if os.environ['OBS_WS_ACTIVE'] == "1":
      cl.set_input_mute(os.environ['AUDIO_SOUCE_NAME'], True)
    playsound.playsound(os.environ['MUSIC_FILE'])
    if os.environ['OBS_WS_ACTIVE'] == "1":
      cl.set_input_mute(os.environ['AUDIO_SOUCE_NAME'], False)

@bot.event
async def event_ready():
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"Бот на месте")


@bot.event
async def event_message(ctx):
    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)



@bot.command(name='zaebal')
async def test(ctx):
    if ctx.author.name in allowed_users:
      do_magic()
      await ctx.send('Исполнено')

with open('allowed_users.txt') as f:
    allowed_users = list(map(lambda x: x.replace("\n",""),f.readlines()))

if os.environ['OBS_WS_ACTIVE'] == "1":
  cl = obs.ReqClient(host='localhost', port=os.environ['OBS_PORT'], password=os.environ['OBS_PASSWORD'], timeout=3)
bot.run()
