class Subscriber:
    def __init__(self, name):
        self.name = name

    def notification(self, info):
        print(f"{self.name} got some {info= }")


class Trashcan:
    def __init__(self, *subscribers: Subscriber):
        self.subscribers = [subscriber for subscriber in subscribers]

    def send_notification(self):
        for subscriber in self.subscribers:
            subscriber.notification("Jestem pełny.")


if __name__ == '__main__':
    user1 = Subscriber("Slack")
    user2 = Subscriber("Teams")
    user3 = Subscriber("Logger")
    user4 = Subscriber("Email")
    trashcan = Trashcan(user1, user2, user3, user4)
    trashcan.send_notification()
