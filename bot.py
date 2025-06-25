from aiogram import Bot, Dispatcher, executor, types
from api import get_token_xl, get_token_session, beli_paket, cek_status

# Bot Telegram API Token
bot = Bot(token="7571605934:AAHKtkmxvD2aNG9Jpwzw_2t46QDvIBMFUjo")
dp = Dispatcher(bot)

# Simpan data user yang pernah start (di memori sederhana)
user_data = set()

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    user_id = msg.from_user.id
    if user_id not in user_data:
        user_data.add(user_id)
        await msg.answer("ðŸ“‹ Kamu telah terdaftar sebagai member baru.")
    await msg.answer("Selamat datang! Gunakan perintah:
/token
/session
/beli
/status")

@dp.message_handler(commands=["token"])
async def token(msg: types.Message):
    data = get_token_xl()
    await msg.answer(f"Access Token:
{data}")

@dp.message_handler(commands=["session"])
async def session(msg: types.Message):
    data = get_token_session()
    await msg.answer(f"Session Token:
{data}")

@dp.message_handler(commands=["beli"])
async def beli(msg: types.Message):
    try:
        _, nomor, paket_id, token = msg.text.split()
        result = beli_paket(nomor, paket_id, token)
        await msg.answer(str(result))
    except Exception as e:
        await msg.answer("Format salah. Gunakan:
/beli 08xxxx paket_id token
Error: " + str(e))

@dp.message_handler(commands=["status"])
async def status(msg: types.Message):
    try:
        _, order_id = msg.text.split()
        result = cek_status(order_id)
        await msg.answer(str(result))
    except Exception as e:
        await msg.answer("Gunakan format: /status IDTransaksi
Error: " + str(e))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
