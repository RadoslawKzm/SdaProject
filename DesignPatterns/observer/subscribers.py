from abc import ABC, abstractmethod


class SubscriberABC(ABC):

    @abstractmethod
    def notify(self, info: str) -> None:
        pass

    @abstractmethod
    def destroy(self, info: str) -> None:
        pass

    @abstractmethod
    def create(self, info: str) -> None:
        pass


class SubscriberSlack(SubscriberABC):
    def __init__(self, name):
        self.name = name

    def notify(self, info: str) -> None:
        print(f"{self.name} got some slack message: {info}")

    def destroy(self, info: str) -> None:
        pass

    def create(self, info: str) -> None:
        pass


class SubscriberTeams(SubscriberABC):
    def __init__(self, name):
        self.name = name

    def notify(self, info: str) -> None:
        print(f"{self.name} got some teams message: {info}")

    def destroy(self, info: str) -> None:
        pass

    def create(self, info: str) -> None:
        pass


class SubscriberEmail(SubscriberABC):
    def __init__(self, name):
        self.name = name

    def notify(self, info: str) -> None:
        print(f"{self.name} got mail sent with message: {info}")

    def destroy(self, info: str) -> None:
        pass

    def create(self, info: str) -> None:
        pass
