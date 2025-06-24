from aiogram import Bot, Dispatcher, executor, types
from api import get_token_xl, get_token_session, beli_paket, cek_status

bot = Bot(token="7921247390:AAHELKsIPDGyqDuybVsYvAeX-Sr0CKBXwfo")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("Selamat datang! Gunakan perintah:\n/token\n/session\n/beli\n/status")

@dp.message_handler(commands=["token"])
async def token(msg: types.Message):
    data = get_token_xl()
    await msg.answer(f"Access Token:\n{data}")

@dp.message_handler(commands=["session"])
async def session(msg: types.Message):
    data = get_token_session()
    await msg.answer(f"Session Token:\n{data}")

@dp.message_handler(commands=["beli"])
async def beli(msg: types.Message):
    try:
        _, nomor, paket_id, token = msg.text.split()
        result = beli_paket(nomor, paket_id, token)
        await msg.answer(str(result))
    except:
        await msg.answer("Format salah. Gunakan:\n/beli 08xxxx paket_id token")

@dp.message_handler(commands=["status"])
async def status(msg: types.Message):
    try:
        _, order_id = msg.text.split()
        result = cek_status(order_id)
        await msg.answer(str(result))
    except:
        await msg.answer("Gunakan format: /status IDTransaksi")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
