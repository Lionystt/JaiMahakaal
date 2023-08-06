# OM NAMAH SHIVAAY
# Application id : 1137640212978221096
# Public key : 8d9953e3723efb640283a4051f761c56cef8da31fb8618d20b42980782ce4d77
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        # await message.channel.send("Harman Welcomes you!")
        match message.content :
          case "Hi":
            await message.channel.send('Hi!')
          case "My name is Harman":
            await message.channel.send('Welcome! Sir')
          case "Jai Mahakaal":
            await message.channel.send('Jai Mahakaal! :pray:')
          case "":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case "Hi":
            await message.channel.send('Hi!')
          case _:
            await message.channel.send("ho")
            

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTEzNzY1MzMzMjU4NDk2ODIyMg.GzlG5j.rt3tBQnwV0fQT-cBLBHZZouOzDF6g53rFmopc4')
