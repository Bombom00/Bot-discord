
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

PALAVRA_PROIBIDA = "xana"

@bot.event
async def on_ready():
    print(f'Bot ligado como {bot.user}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if PALAVRA_PROIBIDA in message.content.lower():
        canal = message.channel
        autor = message.author

        # Apaga a mensagem que ativou
        await message.delete()

        # Pega e apaga mensagens recentes do usuário
        contador = 0
        sem_encontrar = 0

        async for msg in canal.history(limit=50):
            if msg.author == autor:
                try:
                    await msg.delete()
                    contador += 1
                    sem_encontrar = 0
                except:
                    pass
            else:
              sem_encontrar += 1
            if sem_encontrar >= 20:
                 break
            if contador >= 50:
               break

    await bot.process_commands(message)

bot.run("TOKEN")
