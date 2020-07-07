import asyncio
import logging
import random
from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class Mod(loader.Module):
    strings = {"cfg_doc": "This is what is said, you can edit me with the configurator",
               "name": "TestM"}
    def __init__(self):
        self.config = loader.ModuleConfig("CONFIG_STRING", "hello", lambda m: self.strings("cfg_doc", m))


    @loader.unrestricted
    async def examcmd(self, message):
        await utils.answer(message, "WoW")

    async def pentagoncmd(self, message):
        await message.edit("Vzlom Pentagona V1")
        await asyncio.sleep(2)
        async for i in range(102):
	    await message.edit(messge, "Hacking  "+str(i)+" %")
	    await asyncio.sleep(0.1)
        await asyncio.sleep(3)
        await message.edit(message, "Pentagon Hacked!")
