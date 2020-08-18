from telethon import TelegramClient, events


api_id = api_id
api_hash = api_hash 

client = TelegramClient('hello', api_id, api_hash)
async def main():
    me = await client.get_me()
    print(me.stringify())

    username = me.username
    print(username)
    print(me.phone)

    async for dialog in client.iter_dialogs():
         print(dialog.name, 'has ID', dialog.id)

    await client.send_message('homeless kids next door', 'Hello, myself!')     

    await client.send_message('homeless kids next door', 'https://i.ytimg.com/vi/4s5cxNdN9BI/maxresdefault.jpg')  

    await client.send_message('homeless kids next door', 'http://i.huffpost.com/gen/1949203/images/o-HOMELESS-KIDS-facebook.jpg')

    await client. send_message('homeless kids next door', 'https://gaana.com/song/bella-ciao-hugel-remix')
           

with client:
    client.loop.run_until_complete(main())                    





