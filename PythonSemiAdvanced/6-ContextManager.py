with open("test.py", "w") as file2:
    print("pass")


class X:
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
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

with our_open("plik.txt") as file:
    file.write("dupa")

