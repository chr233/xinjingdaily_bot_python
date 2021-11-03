'''
# @Author       : Chr_
# @Date         : 2021-11-02 14:25:11
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-03 23:19:52
# @Description  : 处理投稿
'''

from typing import List
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types.callback_query import CallbackQuery
from aiogram.types.message import Message
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from models.post import Posts, Post_Status

# from buttons.submit import start_keyboard


async def handle_inline(query: CallbackQuery):
    data = query.data
    msg_id = query.message.message_id

    print(data, msg_id)


async def handle_text(message: Message):
    # await message.reply('暂不支持文字投稿哟~')
    # raise CancelHandler()

    print('\n', message.message_id, '\n')

    _keyboard = [
        [InlineKeyboardButton('投稿', callback_data='fine'),
         InlineKeyboardButton('取消', callback_data='fine')],
        [InlineKeyboardButton('匿名', callback_data='not_bad')]
    ]
    # keyboard = types.ReplyKeyboardMarkup(keyboard=_keyboard)

    # await message.reply("Hi!\nHow are you?", reply_markup=keyboard)

    start_keyboard = InlineKeyboardMarkup(inline_keyboard=_keyboard)

    await message.reply('111', reply_markup=start_keyboard)


async def handle_single_post(message: Message):
    print(message.message_id)

    _keyboard = [
        [InlineKeyboardButton('Fine', callback_data='fine')],
        [InlineKeyboardButton('Not bad', callback_data='not_bad')],
        [InlineKeyboardButton('测试', url='https://vk.com/feed')]
    ]
    # keyboard = types.ReplyKeyboardMarkup(keyboard=_keyboard)

    # await message.reply("Hi!\nHow are you?", reply_markup=keyboard)

    start_keyboard = InlineKeyboardMarkup(inline_keyboard=_keyboard)

    await message.reply('111', reply_markup=start_keyboard)


async def handle_mulite_post(messages: List[Message]):
    await messages[0].reply('233')
