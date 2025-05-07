from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

TOKEN = os.getenv("8110018320:AAHqYUR8Z4-6xRiN7TxasC6gA2mVXlmjKXo")
ADMIN_ID = int(os.getenv("921014083"))

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption="📸 Аноним скриншот")

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def handle_document(message: types.Message):
    await bot.send_document(chat_id=ADMIN_ID, document=message.document.file_id, caption="📎 Аноним файл")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text(message: types.Message):
    await bot.send_message(chat_id=ADMIN_ID, text=f"💬 Аноним хат:\n{message.text}")

@dp.message_handler()
async def handle_other(message: types.Message):
    await message.reply("📥 Сәлем! Маған скриншот, файл немесе хабарлама жіберсең, ол аноним түрде иесіне жетеді.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
