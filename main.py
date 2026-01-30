from loguru import logger
import asyncio

from config import Config

NOTIFIERS = [
    ("telegram", "NotifyTelegram"),
    ("sms_mts_exolve", "NotifySMS"),
    ("email", "NotifyEmail")
]


async def run_notifier(notifier, message):
    if asyncio.iscoroutinefunction(notifier.notify_user):
        return await notifier.notify_user(message)
    else:
        return await asyncio.to_thread(notifier.notify_user, message)


async def main():
    config = Config()
    settings = config.get_config_settings()

    is_test_mode = config.test 
    message = settings['message']

    logger.info(f"Starting notification service. Test mode: {is_test_mode}")

    for module_name, class_name in NOTIFIERS:
        try:
            module = __import__(f"notifiers.{module_name}", fromlist=[class_name])
            notifier_class = getattr(module, class_name)
            notifier = notifier_class()

            if await run_notifier(notifier, message):
                logger.success(f"{module_name} notification sent!")
                if not is_test_mode:
                    break

        except Exception as e:
            logger.warning(f"{module_name} failed: {e}")

if __name__ == "__main__":
    asyncio.run(main())
