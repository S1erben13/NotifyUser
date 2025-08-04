from loguru import logger
from aiogram import Bot
from aiogram.enums import ParseMode

from config import Config
from notifiers.base import NotifyBase


class NotifyTelegram(NotifyBase):
    async def notify_user(self, message):
        bot = None
        try:
            config = Config().get_config_telegram()
            bot = Bot(token=config['bot_token'])

            await bot.send_message(
                chat_id=config["target_user_id"],
                text=message,
                parse_mode=ParseMode.HTML
            )
            return True

        except Exception as e:
            logger.error(f"Telegram notification failed: {e}")
            return False
        finally:
            if bot:
                await bot.session.close()