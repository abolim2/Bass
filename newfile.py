from pyrogram import Client
import random
import asyncio
r = ["salam😂", "khobi🤪" , "mikhorish🟢" , "koniii" , "erfanoo9"]
api_id = 29637827
api_hash = "ab31eb5a73c2752708e25a2cacc5a074"
abol = "a2bol"
app = Client("88account", api_id=api_id, api_hash=api_hash)
async def main():
    async with app:
     while True:
         text = random.choice(r)
         await app.send_message(abol,f"{text}")
         await asyncio.sleep(10)
 
app.run(main())
