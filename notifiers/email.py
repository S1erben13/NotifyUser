from loguru import logger
import smtplib
from smtplib import SMTPException

from config import Config
from notifiers.base import NotifyBase


class NotifyEmail(NotifyBase):
    def notify_user(self, text):
        try:
            config = Config().get_config_email()

            message = f"Subject: {config["subject"]}\n\n{text}"

            with smtplib.SMTP(config["domain"], config["port"]) as server:
                server.starttls()
                server.login(config["login"], config["password"])
                server.sendmail(
                    from_addr=config["login"],
                    to_addrs=config["email_target"],
                    msg=message
                )
            return True

        except SMTPException as e:
            logger.error(f"Email sending failed (SMTP error): {e}")
            return False
        except Exception as e:
            logger.error(f"Email sending failed (unexpected error): {e}")
            return False