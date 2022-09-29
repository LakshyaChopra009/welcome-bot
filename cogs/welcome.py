from sqlite3 import Timestamp
import discord
from discord.ext import commands
import datetime

class WelcomeModule(commands.Cog, name='Developer Commands'):
    '''These are the developer commands'''
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Welcome Module Ready')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        Family_Role= [1022167232199000156,1022572003695271966,1021781955391537162,1021781962437963827,1021781956318474301]
        channel = self.bot.get_channel(985583159586459708)
        em = embed=discord.Embed(description="""𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐍ι𝐠нτ 𝐒ταℓκєяѕ<:tsc_smileykiss:986312710541168700>\n \n<a:tsc_love:997038267096649808> ʙᴇ ꜱᴜʀᴇ ᴛᴏ ᴄʜᴇᴄᴋ ᴏᴜᴛ\n<a:arrow_blue:997038188931596338> <#985583140758249472>\n<a:arrow_blue:997038188931596338> <#985583142859571250>\n<a:AUIHug:997529641575251988> ʜᴏᴘᴇ ʏᴏᴜ ᴇɴᴊᴏʏ ꜱᴛᴀʏɪɴɢ ʜᴇʀᴇ <a:tsc_heartlike:997515597619409037>""",timestamp=datetime.datetime.utcnow(), color=0x7105D0)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1021751484112703509/1025104623381516358/dilliwali-namaste-ji.gif")
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        embed.set_image(url="https://media.discordapp.net/attachments/985926436760191106/997092526928437258/welcome_banner_2.gif")
        embed.set_footer(text=f"You are our {member.guild.member_count} member",icon_url=member.guild.icon_url)
        await channel.send(f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 {member.mention} <a:tsc_thanks:986312698398650450>", embed=em)
        for i in Family_Role: 
            await member.add_roles(member.guild.get_role(i))



def setup(bot):
    bot.add_cog(WelcomeModule(bot))
