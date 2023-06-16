import asyncio
import os
from loguru import logger
from aiogram import Bot, Dispatcher, executor, types

logger.level("INFO")
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	await message.reply("我是你爹")


@dp.chat_join_request_handler()
async def join(request: types.ChatJoinRequest):
	user_id = request.from_user.id
	username = request.from_user.username
	chat_id = request.chat.id
	logger.info(f"{username}({user_id}) is requesting to join {chat_id}.")
	message = await bot.send_message(chat_id, f"@{username}({user_id}) is requesting to join this group.")
	await bot.pin_chat_message(chat_id, message.message_id)
	polling = await bot.send_poll(
		chat_id,
		"Approve this user?",
		["Yes", "No"],
		is_anonymous=True,
		allows_multiple_answers=False,
		reply_to_message_id=message.message_id,
	)
	await asyncio.sleep(300)
	await bot.unpin_chat_message(chat_id, message.message_id)
	polling = await bot.stop_poll(chat_id, polling.message_id)

	if polling.total_voter_count == 0:
		await message.reply("No one voted.")
		await bot.send_message(user_id, "No one voted. Please request again later.")
		logger.info(f"No one voted for {username}({user_id}) in chat {chat_id}.")
		await request.decline()
	elif polling.options[0].voter_count > polling.options[1].voter_count:
		await message.reply("Approved.")
		await bot.send_message(user_id, "You have been approved.")
		logger.info(f"{username}({user_id}) has been approved in chat {chat_id}.")
		await request.approve()
	elif polling.options[0].voter_count == polling.options[1].voter_count:
		await message.reply("No result.")
		await bot.send_message(user_id, "No result. Please request again later.")
		logger.info(f"No result for {username}({user_id}) in chat {chat_id}.")
		await request.decline()
	else:
		await message.reply("Denied.")
		await bot.send_message(user_id, "You have been denied.")
		logger.info(f"{username}({user_id}) has been denied in chat {chat_id}.")
		await request.decline()


if __name__ == '__main__':
	executor.start_polling(dp)
