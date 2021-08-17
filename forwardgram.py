from telethon import TelegramClient, events, sync

# +380985213131

SESSION_KEY = "just_pass_same_key_to_save_session"
API_ID = "3364871" #from tg site
API_HASH = "20c0b4b08bab4f08bb21cdc409167607"#from tg site

redirect_started_welcome_message = "REDIRECT STARTED, LET`s DO MONEY"
CHANNEL_TO_REDIRECT_IN = "redirect"
CHANNELS_TO_REDIRECT_FROM = ['CM Margin: Rose Bitmex premium',
                             'CM Core: Inner Circle Chat']

if __name__ == "__main__":
    client = TelegramClient(SESSION_KEY,
                            API_ID,
                            API_HASH)
    client.start()
    client.send_message(CHANNEL_TO_REDIRECT_IN, redirect_started_welcome_message)
    @client.on(events.NewMessage(chats=CHANNELS_TO_REDIRECT_FROM))
    async def handler(event):
        await client.forward_messages(CHANNEL_TO_REDIRECT_IN, event.message)
    client.run_until_disconnected()

