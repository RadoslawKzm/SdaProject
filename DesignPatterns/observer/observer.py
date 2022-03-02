from typing import Protocol

from subscribers import SubscriberSlack, SubscriberEmail, SubscriberTeams


class Notifiable(Protocol):
    def notify(self, info: str) -> None:
        ...


class Trashcan:
    def __init__(self, *subscribers: Notifiable):
        self.subscribers = [subscriber for subscriber in subscribers]

    def send_notification(self):
        for subscriber in self.subscribers:
            subscriber.notify("I'm full")


if __name__ == '__main__':
    slack = SubscriberSlack("Slack")
    teams = SubscriberTeams("Teams")
    email = SubscriberEmail("Email")
    trashcan = Trashcan(slack, teams, email)
    trashcan.send_notification()
