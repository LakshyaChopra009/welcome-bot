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
        Family_Role= [1025734170405765180,1025734224323543100,1025734214659866644,1025734215662321684,1025734216153042975]
        channel = self.bot.get_channel(1126564299574366350)
        em = embed=discord.Embed(description="""Welcome to 𝐆υρѕнυρ <a:zz_cheers:1136590964199272458>\n \n<a:tsc_love:997038267096649808> ʙᴇ ꜱᴜʀᴇ ᴛᴏ ᴄʜᴇᴄᴋ ᴏᴜᴛ\n<a:arrow_blue:997038188931596338> <#1043481661280620574>\n<a:arrow_blue:997038188931596338> <#1043481658382368819>\n<a:AUIHug:997529641575251988> ʜᴏᴘᴇ ʏᴏᴜ ᴇɴᴊᴏʏ ꜱᴛᴀʏɪɴɢ ʜᴇʀᴇ <a:tsc_heartlike:997515597619409037>""",timestamp=datetime.datetime.utcnow(), color=0x7105D0)
        em.set_thumbnail(url="https://media.discordapp.net/attachments/1021751484112703509/1025104623381516358/dilliwali-namaste-ji.gif")
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        embed.set_image(url="https://media.discordapp.net/attachments/985926436760191106/997092526928437258/welcome_banner_2.gif")
        embed.set_footer(text=f"You are our {member.guild.member_count} member",icon_url=member.guild.icon_url)
        await channel.send(f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 {member.mention} <a:tsc_thanks:986312698398650450>", embed=em)
        for i in Family_Role: 
            await member.add_roles(member.guild.get_role(i))

    @commands.command()
    async def testgreet(self,ctx):
        channel = self.bot.get_channel(1126564299574366350)
        em = embed=discord.Embed(description="""𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐍ι𝐠нτ 𝐒ταℓκєяѕ<:tsc_smileykiss:986312710541168700>\n \n<a:tsc_love:997038267096649808> ʙᴇ ꜱᴜʀᴇ ᴛᴏ ᴄʜᴇᴄᴋ ᴏᴜᴛ\n<a:arrow_blue:997038188931596338> <#1043481661280620574>\n<a:arrow_blue:997038188931596338> <#1043481658382368819>\n<a:AUIHug:997529641575251988> ʜᴏᴘᴇ ʏᴏᴜ ᴇɴᴊᴏʏ ꜱᴛᴀʏɪɴɢ ʜᴇʀᴇ <a:tsc_heartlike:997515597619409037>""",timestamp=datetime.datetime.utcnow(), color=0x7105D0)
        em.set_thumbnail(url="https://media.discordapp.net/attachments/1021751484112703509/1025104623381516358/dilliwali-namaste-ji.gif")
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        embed.set_image(url="https://media.discordapp.net/attachments/985926436760191106/997092526928437258/welcome_banner_2.gif")
        embed.set_footer(text=f"You are our {member.guild.member_count} member",icon_url=member.guild.icon_url)
        await channel.send(f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 {member.mention} <a:tsc_thanks:986312698398650450>", embed=em)
        await channel.send("``` Please Note Bot will not add any family role while using testgreet command ```")
def setup(bot):
    bot.add_cog(WelcomeModule(bot))
