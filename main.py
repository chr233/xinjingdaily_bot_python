'''
# @Author       : Chr_
# @Date         : 2021-10-27 13:12:21
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-02 14:23:52
# @Description  : 
'''

from aiogram import Bot, Dispatcher, executor

from config import CFG, Bot_Modes

from db import init_orm, close_orm

from command.user import setup as user_setup
from command.admin import setup as admin_setup

from middleware.user_login import UserLogin

def main():
    '''启动函数'''

    bot = Bot(token=CFG.Bot_Token)
    dispatcher = Dispatcher(bot)

    dispatcher.middleware.setup(UserLogin())

    startups = [
        init_orm,
        user_setup,
        admin_setup,
    ]
    shutdowns = [close_orm]

    if CFG.Bot_Mode == Bot_Modes.P:
        executor.start_polling(
            dispatcher,
            on_startup=startups,
            on_shutdown=shutdowns
        )
    else:
        executor.start_webhook(
            dispatcher,
            on_startup=startups,
            on_shutdown=shutdowns
        )


if __name__ == '__main__':
    main()
