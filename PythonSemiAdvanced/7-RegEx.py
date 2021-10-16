"""

\d
\w
+
?

"""

import re

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
from abc import ABC, abstractmethod


class User(ABC):
    """Each subclass has to have name"""

    @classmethod
    def as_dict(cls):
        return {obj.name: obj for obj in cls.__subclasses__()}

    @abstractmethod
    def woof(self) -> None:
        """implement woofing"""

    @classmethod
    def update_list(cls, *, self):
        cls.gender_list.append(self)


class Female(User):
    name: str = "female"
    gender_list: list = []

    def __init__(self, *, first_name: str, last_name: str, email: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def woof(self) -> None:
        print(f"Yes daddy! {self.name}")


class Male(User):
    name: str = "male"
    gender_list: list = []

    def __init__(self, *, first_name: str, last_name: str, email: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def woof(self) -> None:
        print("Woff woof!")


def first():
    with open("7-RegEx_example2", encoding='cp850') as file:
        line = file.readline()
        users = re.split(r"(?={\"gender)", line)[1:]
        for user in users:
            email = re.findall(r"(?<=\"email\":\")[a-zA-z.@]*", user)[0]
            gender = re.findall(r"(?<=\"gender\":\")[a-zA-z.@]*", user)[0]
            firstname = re.findall(r"(?<=,\"first\":\")[a-zA-z.@]*", user)[0]
            lastname = re.findall(r"(?<=,\"last\":\")[a-zA-z.@]*", user)[0]
            age = re.findall(r"(?<=,\"age\":)[0-9]*(?=},\"registered\")", user)[0]
            User.as_dict()[gender](first_name=firstname, last_name=lastname, email=email, age=age)


def second():
    pass


print(Female)
