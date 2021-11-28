from subscribers import SubscriberABC, SubscriberSlack, SubscriberEmail, SubscriberTeams


class Trashcan:
    def __init__(self, *subscribers: SubscriberABC):
        self.subscribers = [subscriber for subscriber in subscribers]

    def send_notification(self):
        for subscriber in self.subscribers:
            subscriber.notification("Jestem pełny.")


if __name__ == '__main__':
    slack = SubscriberSlack("Slack")
    teams = SubscriberTeams("Teams")
    email = SubscriberEmail("Email")
    trashcan = Trashcan(slack, teams, email)
    trashcan.send_notification()
