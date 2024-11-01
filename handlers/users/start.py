from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.start_menu import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text=f"Assalomu Alaykum {message.from_user.full_name}!\n\n"
    text+=f"Sizni IT TAT Telegram Botida Ko'rganimizdan xursandmiz 🙂\n\n"
    text+=f"Bizning bot orqali\n"
    text+=f"-Mavjud kurslar bilan tanishishingiz\n"
    text+=f"-Kurslarga ro'yxatdan o'tishingiz\n"
    text+=f"-Yangiliklar haqida xabardor bo'lib turishingiz mumkin\n"
    text+=f"Boshlash uchun quyidagi menyudan tanlang va biz haqimizda ma'lumot oling"
    await message.answer(text,reply_markup=menu,parse_mode="Markdown")
