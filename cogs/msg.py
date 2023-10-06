import discord,json
import datetime
from discord import app_commands
from discord.ext import tasks, commands
from discord.ext import commands
# 導入core資料夾中的自寫模組
from core.classes import Cog_Extension

with open("setting/channel.json","r",encoding='UTF-8') as f:
    chaid = json.load(f)
with open("setting/role.json","r",encoding='UTF-8') as f:
    role = json.load(f)

class Msg(Cog_Extension):
    @app_commands.command(name="contribute",description="指令教學")
    async def contribute(self, interaction: discord.Interaction):
        embed=discord.Embed(title="🏫 NASH 投稿提示", color=0xb8d8af,timestamp=datetime.utcnow())
        embed.add_field(name="", value="``` " + role["check"].mention + " 嗨嗨 我是輔導主任 \n歡迎至" + int(chaid['service']).mention + "幫我投稿回應句喔```\n投稿格式:\n```關鍵字:\n回應內容:```", inline=False)
        await interaction.response.send_message(embed=embed)
    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        channel_id = int(chaid['counseling'])
        if message.author == self.bot.user:
            return
        if message.content == "Hello" and message.channel.id == channel_id:
            await message.channel.send("Hello, world!")


# 載入cog中
async def setup(bot):
    await bot.add_cog(Msg(bot))