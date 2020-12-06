import asyncio
from telethon import events
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import ALIVE_NAME, MLO Version
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Mlo KING"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/45c40f478c0d02ff317fd.jpg"
pm_caption = "__**🔥🔥🙋JINDAA HU SIR🙋🔥🔥**__\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={PROFESSOR})』**\n\n"

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"😈Mlo User😈       : `{mloversion}`\n"

pm_caption += f"⚜️Sudo⚜️            : `{sudou}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/MLO_USERBOT)\n"

pm_caption += "🔥CREATOR🔥    : [SUR Here](https://t.me/MBBS_LOVER)\n\n"

pm_caption += "      [✨REPO✨](https://github.com/Prashu1708/MLO-BOT

@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
