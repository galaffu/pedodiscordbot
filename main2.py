import discum
import discord
from discord.ext import commands

client = discord.Client()


bot = discum.Client(token="ODk3MTgxMTE3ODMxMDg2MTAx.YWR7qg.be-BkFr_IMHquLbD8JvjzlFggZ0")

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members

members = get_members('879468149924315247', '879468149924315251')
memberslist = []


for memberID in members:
    memberslist.append(memberID)
    print(memberID)
    


f = open('users.txt', "a")
for element in memberslist:
    f.write(element + '\n')
f.close()