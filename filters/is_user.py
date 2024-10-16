from aiogram.types import Message
from aiogram.filters import Filter
from data.config import ADMINS

class IsUser(Filter):

    async def check(self, message: Message):
        return message.from_user.id not in ADMINS
