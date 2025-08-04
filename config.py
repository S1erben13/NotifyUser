from loguru import logger
import os
from dotenv import load_dotenv

class ConfigCheckMixin:
    def is_there_all_required_fields(self):
        for name, value in vars(self).items():
            if not name.startswith('_') and value is None:
                raise ValueError(f"Attribute '{name}' is None!")
        return True


class ConfigEmail(ConfigCheckMixin):
    def __init__(self):
        self.domain = os.getenv("DOMAIN")
        self.port = os.getenv("PORT")
        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")
        self.email_target = os.getenv("EMAIL_TARGET")
        self.subject = os.getenv("EMAIL_SUBJECT")

    def get_config_email(self):
        try:
            if self.is_there_all_required_fields():
                port = int(self.port)
                return {"domain": self.domain, "port": port, "login": self.login,
                        "password": self.password, "email_target": self.email_target, "subject": self.email_target}
        except Exception as e:
            logger.error(f"Error in email config: {e}")
        return None


class ConfigTelegram(ConfigCheckMixin):
    def __init__(self):
        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.target_user_id = os.getenv("TELEGRAM_USER_ID_TARGET")

    def get_config_telegram(self):
        try:
            if self.is_there_all_required_fields():
                target_user_id = int(self.target_user_id)
                return {"bot_token": self.bot_token, "target_user_id": target_user_id}
        except Exception as e:
            logger.error(f"Error in telegram config: {e}")
        return None


class ConfigSMS(ConfigCheckMixin):
    """Sending sms via MTS Exolve"""
    def __init__(self):
        self.phone_number_target = os.getenv("PHONE_NUMBER_TARGET")
        self.phone_number_app = os.getenv("PHONE_NUMBER_APP")
        self.api_key = os.getenv("API_KEY")

    def get_config_sms(self):
        try:
            if self.is_there_all_required_fields():
                return {"phone_number_target": self.phone_number_target, "phone_number_app": self.phone_number_app, "api_key": self.api_key, }
        except Exception as e:
            logger.error(f"Error in SMS config: {e}")
        return None

class ConfigSettings(ConfigCheckMixin):
    def __init__(self):
        self.test = (os.getenv('TEST', 'False') == 'True')
        self.message = os.getenv("MESSAGE")

    def get_config_settings(self):
        try:
            if self.is_there_all_required_fields():
                return {"message": self.message}
        except Exception as e:
            logger.error(f"Error in SMS config: {e}")
        return None


class Config(ConfigEmail, ConfigTelegram, ConfigSMS, ConfigSettings):
    def __init__(self, env_file=None):
        if env_file:
            load_dotenv(env_file)
        else:
            load_dotenv()
        ConfigEmail.__init__(self)
        ConfigTelegram.__init__(self)
        ConfigSMS.__init__(self)
        ConfigSettings.__init__(self)
