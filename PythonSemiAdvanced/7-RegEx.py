"""

\d
\w
+
?

"""

import re
from abc import ABC, abstractmethod
from time import time


# strin = "test 123_du1pa+test"
# output_1 = re.sub(r"[ _+]", "", strin)
# output_2 = re.findall(r"[dupa]", strin)
# compiled_regex = re.compile(r"[dupa]")
# output_3 = re.findall(compiled_regex, strin)
# output_4 = re.match(r"d", strin)
# output_5 = re.search(r"dupa", strin)

# st: set = set()
#
# with open("7-RegEx_example", "r") as file:
#     for line in file:
#         if text := re.findall(r"(?<=\* Cell {13}: )\w+", line):
#             st.add(text[0].strip())


class User(ABC):
    gender_list: list = []
    index_: int = 0

    @classmethod
    def as_dict(cls):
        return {obj.name: obj for obj in User.__subclasses__()}

    @classmethod
    def update_list(cls, *, self):
        cls.gender_list.append(self)

    @classmethod
    def __str__(cls):
        return "dupa"

    @abstractmethod
    def woof(self) -> None:
        pass


class Male(User):
    gender_list: list = []
    name: str = "male"

    def __init__(self, *, first: str, last: str, age: int, mail: str):
        self.first = first
        self.last = last
        self.age = age
        self.mail = mail
        self.update_list(self=self)

    def woof(self) -> None:
        print(f"{self.name}")


class Female(User):
    gender_list: list = []
    name: str = "female"

    def __init__(self, *, first: str, last: str, age: int, mail: str):
        self.first = first
        self.last = last
        self.age = age
        self.mail = mail
        self.update_list(self=self)

    def woof(self) -> None:
        print(f"{self.name}")


def time_measure(function):
    def wrapper(*args, **kwargs):
        startpoint = time()
        function(*args, **kwargs)
        return f"Funkcja {function.__name__} zajęła {(time() - startpoint):.2f} sekund"

    return wrapper


@time_measure
def first():
    with open("7-RegEx_example2", encoding="cp850") as file:
        line = file.readline()
        users = re.split(r"(?={\"gender)", line)[1:]
        for user in users:
            email = re.findall(r"(?<=\"email\":\")[a-zA-z.@]*", user)[0]
            name = re.findall(r"(?<=\"first\":\")[a-zA-z.@]*", user)[0]
            last = re.findall(r"(?<=\"last\":\")[a-zA-z.@]*", user)[0]
            age = re.findall(r"(?<=,\"age\":)[0-9]*(?=},\"registered\")", user)[0]
            gender = re.findall(r"(?<=\"gender\":\")[a-zA-z.@]*", user)[0]
            User.as_dict()[gender](first=name, last=last, age=age, mail=email)


@time_measure
def second():
    with open("7-RegEx_example2", encoding="cp850") as file:
        line = file.readline()
        users = re.split(r"(?={\"gender)", line)[1:]
        email_compile = re.compile(r"(?<=\"email\":\")[a-zA-z.@]*")
        name_compile = re.compile(r"(?<=\"first\":\")[a-zA-z.@]*")
        last_compile = re.compile(r"(?<=\"last\":\")[a-zA-z.@]*")
        age_compile = re.compile(r"(?<=,\"age\":)[0-9]*(?=},\"registered\")")
        gender_compile = re.compile(r"(?<=\"gender\":\")[a-zA-z.@]*")
        for user in users:
            email = re.findall(email_compile, user)[0]
            name = re.findall(name_compile, user)[0]
            last = re.findall(last_compile, user)[0]
            age = re.findall(age_compile, user)[0]
            gender = re.findall(gender_compile, user)[0]
            User.as_dict()[gender](first=name, last=last, age=age, mail=email)


if __name__ == '__main__':
    print(first())
    print(second())
