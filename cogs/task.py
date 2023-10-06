import discord,json
import datetime

from discord.ext import tasks, commands
from discord.ext import commands
# 導入core資料夾中的自寫模組
from core.classes import Cog_Extension

with open("setting/channel.json","r",encoding='UTF-8') as f:
    chaid = json.load(f)

class Task(Cog_Extension):
        # 臺灣時區 UTC+8
        tz = datetime.timezone(datetime.timedelta(hours = 8))
        # 設定每日十二點執行一次函式
        night = datetime.time(hour = 0, minute = 0, tzinfo = tz)

        # 每日十二點發送 "晚安!瑪卡巴卡!" 訊息
        @tasks.loop(time = night)
        async def everyday(self):
            # 設定發送訊息的頻道ID
            channel_id = chaid['counseling']
            channel = self.bot.get_channel(channel_id)
            embed = discord.Embed(
                title = "該睡囉! 晚安各位",
                description = f"🕛 現在時間 {datetime.date.today()} 00:00",
                color = discord.Color.orange()
            )
            await channel.send(embed = embed)

        # 設定每日十二點執行一次函式
        morning = datetime.time(hour = 7, minute = 0, tzinfo = tz)
        # 每日十二點發送 "晚安!瑪卡巴卡!" 訊息
        @tasks.loop(time = morning)
        async def everyday(self):
            # 設定發送訊息的頻道ID
            channel_id = chaid['counseling']
            channel = self.bot.get_channel(channel_id)
            embed = discord.Embed(
                title = "該上學囉! 早安各位",
                description = f"🕛 現在時間 {datetime.date.today()} 00:00",
                color = discord.Color.to_rgb(149,243,168)
            )
            await channel.send(embed = embed)
        
                # 設定每日十二點執行一次函式
        noon = datetime.time(hour = 12, minute = 0, tzinfo = tz)
        # 每日十二點發送 "晚安!瑪卡巴卡!" 訊息
        @tasks.loop(time = noon)
        async def everyday(self):
            # 設定發送訊息的頻道ID
            channel_id = chaid['counseling']
            channel = self.bot.get_channel(channel_id)
            embed = discord.Embed(
                title = "該吃飯囉~ 誰還沒吃?",
                description = f"🕛 現在時間 {datetime.date.today()} 00:00",
                color = discord.Color.to_rgb(254,255,201)
            )
            await channel.send(embed = embed)


# 載入cog中
async def setup(bot):
    await bot.add_cog(Task(bot))