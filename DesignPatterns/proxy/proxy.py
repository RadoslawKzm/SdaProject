class Database:
    def __init__(self):
        self.data: list = []

    def insert(self, item):
        self.data.append(item)

    def insert_many(self, *items):
        self.data.extend(items)

    def get(self):
        print("getteing from db")
        return [item for item in range(10_000_000)]


def main(database):
    return database.get()


if __name__ == '__main__':
    database = Database()
    print(main(database))
    print(main(database))
    print(main(database))
    print(main(database))
    print(main(database))
