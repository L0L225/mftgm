
import asyncio
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class Test(loader.Module):
    """HZ"""
    strings = {"cfg_doc": "This is what is said, you can edit me with the configurator",
               "name": "Назва модуля",
               "after_sleep": "We have finished sleeping!"}


    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def examplecmd(self, message):
    
        """Does something when you type .example (hence, named examplecmd)"""
        
        logger.debug("We logged something!")
        await utils.answer(message, self.config["CONFIG_STRING"])
        await asyncio.sleep(5)  # Never use time.sleep
        await utils.answer(message, self.strings("after_sleep", message))
