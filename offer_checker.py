from telethon import TelegramClient, events
from env import api_id, api_hash, phone_number # This file is not on the repo because im not a dumbass

keywords = ['rtx', 'error'] # The keywords to seach on the messages
target_channels = ['@OfertonesMexico', '@OFERTAS_PERRONAS', '@ofertasVIPmexicoficial'] # The channels we want to monitor (ID or username)
client = TelegramClient('Offer_tracker', api_id, api_hash)

@client.on(events.NewMessage(chats=target_channels)) # Only check on the selected channels
async def handler(event):
	try:
		message_text = event.message.message
		if any(keyword.lower() in message_text.lower() for keyword in keywords):
			print(f"Matched message in channel {event.chat.title or event.chat.id}: {message_text}")
			await client.send_message('me', message_text)  # Resend message to myself
			print("Message sent")
	except Exception as e:
		print(f"Error handling message: {e}")
		# try:
		# 	# Get channel entity again
		# 	entity = await client.get_entity(event.chat.id)
		# 	print(f"Entity resolved: {entity}")
		# except Exception as inner_e:
		# 	print(f"Failed to resolve entity: {inner_e}")

async def main():
	await client.start(phone_number)
	
	print('Connected and searching for matches on selected channels:')
	for channel in target_channels:
		print(channel)

	# print("Available channels:")
	# async for dialog in client.iter_dialogs():
	# 	print(f"Name: {dialog.name}, ID: {dialog.id}")

	await client.run_until_disconnected()

with client:
	client.loop.run_until_complete(main())