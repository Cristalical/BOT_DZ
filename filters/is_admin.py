from aiogram.types import Message
from aiogram.filters import Filter
from data.config import ADMINS


class IsAdmin(Filter):

    async def check(self, message: Message):
        return message.from_user.id in ADMINS
