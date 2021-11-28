import datetime
import time


class Database:
    def get(self):
        print("getteing from db")
        time.sleep(3)
        return [item for item in range(10)]


class Proxy:
    def __init__(self):
        self.last_query_time = 0
        self.last_query_result = 0

    def get(self, database: Database):
        now = datetime.datetime.now()
        try:
            if (now - self.last_query_time).seconds < 300:
                self.last_query_time = now
                return self.last_query_result
        except TypeError:
            self.last_query_time = now
            self.last_query_result = database.get()
            return self.last_query_result

if __name__ == '__main__':
    database = Database()
    proxy = Proxy()
    proxy.get(database)
    proxy.get(database)
    proxy.get(database)
    proxy.get(database)
    proxy.get(database)
    proxy.get(database)
