with open("test.py", "w") as file2:
    print("pass")


class X:
    def __init__(self, file_name: str):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


file = open("test.py", "w")
try:
    file.write("some dummy line")
finally:
    file.close()


class our_open:
    def __init__(self, file_name: str, method: str = "rt"):
        self.file_name = file_name
        self.method = method

    def __enter__(self):
        self.file_obj = open(self.file_name, self.method)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with our_open("plik.txt", "w") as file:
    file.write("dupa22")
