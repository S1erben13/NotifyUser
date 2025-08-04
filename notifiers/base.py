from abc import ABC, abstractmethod


class NotifyBase(ABC):
    @abstractmethod
    def notify_user(self, message):
        pass




