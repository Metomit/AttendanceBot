import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '--attendance':
            kanals = message.guild.channels
            kanal = None
            for kana in kanals:
                if kana.id == 993596986085351434:
                    kanal = kana
                    break
            mems = message.author.voice.channel.members
            date_time = message.created_at.strftime("%m/%d/%Y")
            attendants = ""
            attendants = attendants + message.author.voice.channel.name + "  --------  " + date_time + "\n\n"
            for mem in mems:
                attendants = attendants + mem.nick + "\n\n"
            await kanal.send(attendants)

client = MyClient()
client.run('token')