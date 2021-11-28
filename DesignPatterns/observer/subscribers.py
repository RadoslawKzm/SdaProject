from abc import ABC, abstractmethod


class SubscriberABC(ABC):

    @abstractmethod
    def notification(self, info: str) ->None:
        pass


class SubscriberSlack(SubscriberABC):
    def __init__(self, name):
        self.name = name

    def notification(self, info: str) -> None:
        print(f"{self.name} got some slack message: {info}")


class SubscriberTeams(SubscriberABC):
    def __init__(self, name):
        self.name = name

    def notification(self, info: str) -> None:
        print(f"{self.name} got some teams message: {info}")


class SubscriberEmail(SubscriberABC):
    def __init__(self, name):
        self.name = name

    def notification(self, info: str) -> None:
        print(f"{self.name} got mail sent with message: {info}")