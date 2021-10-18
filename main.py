import discum
import discord
import time
from discord.ext.commands import Bot
import random

client = discord.Client()

bot1 = Bot("!")
bot = discum.Client(
    token="NzkzOTQ5MjQzMTUyNDAwMzg2.YWXZRQ.A4pIVYRFzvbYzlbw4pLHOlOC1eA")


def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand(
            {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()


def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching,
                        'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members


members = get_members('894670523949264967', '894671075860942908')
memberslist = []


@bot1.command(name="msg", pass_context=True)
async def msg(context, memberID, message):
    user = client.get_user(int(memberID))
    await context.send(message)

for memberID in members:
    memberslist.append(memberID)
    print(memberID)
    num1 = random.randint(603, 1095)
    print(num1)
    newId = str(memberID)
    newDM = bot.createDM([newId]).json()["id"]
    bot.sendMessage(newDM, "https://discord.com/invite/vCVRnqru4h")
    time.sleep(num1)


f = open('users.txt', "a")
for element in memberslist:
    f.write(element + '\n')
f.close()
