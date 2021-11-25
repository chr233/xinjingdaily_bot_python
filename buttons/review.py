'''
# @Author       : Chr_
# @Date         : 2021-11-03 19:46:43
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-25 23:58:42
# @Description  : 审核按钮
'''
from typing import Dict, List, Tuple
from aiogram.types.inline_keyboard import InlineKeyboardButton as IKButon, InlineKeyboardMarkup
from loguru import logger

from utils.emojis import GHOST, SMILE, NO, YES, WATER, CHECK, UNCHECK

from models.tag import StaticTags
from models.reason import Reasons


class ReviewPostKey():
    accept = 'rp_accept'  # 接受投稿
    reject = 'rp_reject'  # 拒绝投稿
    tag = 'rp_tag'  # 拒绝投稿


class ReviewKeyboardsHelper():
    ready = False

    __tags_short: List[Tuple[int, str]] = None
    __tags_full: List[Tuple[int, str]] = None
    __reason: List[str] = None

    __buttons: List[Tuple[str, str]] = None

    def __init__(self) -> None:
        ...

    async def get_tag(self, selected: int) -> str:
        if not self.ready:
            await self.prepare_modules()

        if not selected or selected == 0:
            return ''

        tags = [
            f'#{name}' for id, name in self.__tags_full if selected & id
        ]

        return ' '.join(tags)

    async def prepare_modules(self):
        reasons = await Reasons.all()
        self.__reason = [reason.reason for reason in reasons]

        self.__tags_short = [(x, y[0]) for x, y in StaticTags.items()]
        self.__tags_full = [(x, y[1]) for x, y in StaticTags.items()]

        self.__buttons = [
            (f'{NO}拒绝', ReviewPostKey.reject), (f'{YES}采用', ReviewPostKey.accept)
        ]

        logger.debug('初始化ReviewKeyboardsHelper完成')

        self.ready = True

    async def get_tag_keyboard_short(self, selected: int):
        if not self.ready:
            await self.prepare_modules()

        kbd = [
            [IKButon((CHECK if selected & id else UNCHECK) + name,
                     callback_data=f'{ReviewPostKey.tag} {selected ^ id}')
                for id, name in self.__tags_short],
            [IKButon(text, callback_data=f'{data} {selected}')
                for text, data in self.__buttons]
        ]

        return InlineKeyboardMarkup(inline_keyboard=kbd)

    async def get_tag_keyboard_full(self, selected: int):
        if not self.ready:
            await self.prepare_modules()

        kbd = [
            [IKButon((CHECK if selected & id else UNCHECK) + name,
                     callback_data=f'{ReviewPostKey.tag} {selected ^ id}')
                for id, name in self.__tags_full],
            [IKButon(text, callback_data=f'{data} {selected}')
                for text, data in self.__buttons]
        ]

        return InlineKeyboardMarkup(inline_keyboard=kbd)


RKH = ReviewKeyboardsHelper()
