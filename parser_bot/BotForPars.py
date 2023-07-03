import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import CommandStart
from Keyboard import Key_Pars
import My_token
import asyncio
from Parser_Anic import Pars_Slov, sort_def, sort_on
from Parser_crypts import output_name_coins
import requests



bot = Bot(token=My_token.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(CommandStart())
async def Start(msg: types.Message):
    await msg.reply(f'Здраствуй {msg.from_user.username}', reply_markup=Key_Pars)


@dp.message_handler()
async def ouyput_us(msg: types.Message):
    def User_Sort(sort, input_args):
        if int(input_args) <= sort[1] and int(input_args) != 0:
            return sort[0][int(input_args)]
        else:
            return 'Такого значения нет'
    User_Sort = User_Sort(sort_on, msg.text)
    await msg.answer(User_Sort)


@dp.callback_query_handler(text='Pars_Anic')
async def New_Dialog(cbq: types.CallbackQuery):
    await bot.answer_callback_query(cbq.id)
    for i in sort_on[0]:
        await bot.send_message(cbq.from_user.id, sort_on[0][i])
    await bot.send_message(cbq.from_user.id, f'Всего {i} текстов')


@dp.callback_query_handler(text='Pars_Cripts')
async def callback_process(cbq: types.CallbackQuery):
    list_name_coins = []
    count = -1
    await bot.answer_callback_query(cbq.id)
    output_name_coins()
    for i in range(int(len(output_name_coins()[0] + output_name_coins()[1]) / 2)):
        count += 1
        await bot.send_message(cbq.from_user.id, (f'Название: {output_name_coins()[0][count]},'
                                                  f' цена в USD: {output_name_coins()[1][count]}'))



if __name__ == '__main__':
    executor.start_polling(dp)