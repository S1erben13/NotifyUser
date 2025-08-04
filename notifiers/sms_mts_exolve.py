import requests
from loguru import logger

from config import Config
from notifiers.base import NotifyBase


class NotifySMS(NotifyBase):
    def notify_user(self, message):
        try:
            api_url = "https://api.exolve.ru/messaging/v1/SendSMS"
            config = Config().get_config_sms()

            payload = {
                "number": config["phone_number_app"],
                "destination": config["phone_number_target"],
                "text": message
            }

            headers = {
                "Authorization": f"Bearer {config['api_key']}",
                "Content-Type": "application/json"
            }

            response = requests.post(api_url, json=payload, headers=headers)

            return response.status_code == 200

        except Exception as e:
            logger.error(f"SMS sending failed: {e}")
            return False