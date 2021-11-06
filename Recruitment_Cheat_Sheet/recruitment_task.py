"""
Tell me what is __subclasses__ method, how does it work and what is return of this class. Web search available.
Tell me about Strategy design pattern. How does it work and what is real life python application.. Web search available.
Do below task:
Depending of incoming parameter apply some action. Parameter in range 1:3 including.
if param==1 >> print("Nothing to add")
if param==2 >> print("Something is happening")
if param==3 >> print("Big numbers incoming")
else print("Parameter outside of scope")
Create function that takes parameter. Inside function apply logic that will react to parameter state.

"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Union

"""
Insider notes not for candidate. What we are checking:
- how function is created, is annotation used?
- will he use if name main in program.
- will he make if-land or maybe dictionary, maybe strategy pattern?
- will he use ABC module?
- will he use subclasses method?
Task is aimed to 1st see how candidate can search through web for solutions.
2nd aim is to see how he applies found information to real cases.
We will clearly see on what level candidate is and what code he will produce in our repo. 
We will test him even if he doesn't know something how swift is he and his potential of fast growing up.
"""


def tier_1_solution(param):
    """Basic junior level function. Future code will be full of if-lands and will be not swift according to SOLID.
    Ask for adding case for number 4 without changing function"""
    if param == 1:
        print("Nothing to add")
    elif param == 2:
        print("Something is happening")
    elif param == 3:
        print("Big numbers incoming")
    else:
        print("Parameter outside of scope")


def tier_2_solution(param: int) -> None:
    """Better solution avoiding if-land. Code still not swift according to SOLID.
    Ask for adding case for number 4 without changing function"""
    dictio: dict = {1: "Nothing to add", 2: "Something is happening", 3: "Big numbers incoming"}
    print(dictio.get(param, "Parameter outside of scope"))


class StrategyABC(ABC):
    name = "placeholder"

    @staticmethod
    @abstractmethod
    def get_string() -> str:
        """implement printing function"""

    @classmethod
    def as_dict(cls) -> Dict[Union[int, str], StrategyABC]:
        return {subclass.name: subclass.get_string() for subclass in cls.__subclasses__()}


class Strategy1(StrategyABC):
    name = 1

    @staticmethod
    def get_string() -> str:
        return "Nothing to add"


class Strategy2(StrategyABC):
    name = 2

    @staticmethod
    def get_string() -> str:
        return "Something is happening"


class Strategy3(StrategyABC):
    name = 3

    @staticmethod
    def get_string() -> str:
        return "Big numbers incoming"


class StrategyFallback(StrategyABC):
    name = "Exception"

    @staticmethod
    def get_string() -> str:
        return "Parameter outside of scope"


def tier_3_solution(param: int) -> None:
    """Advanced typing used. Code is swift, adding new number without changing function itself"""
    strategies = StrategyABC.as_dict()
    print(strategies.get(param, strategies["Exception"]).get_string())


if __name__ == '__main__':
    tier_1_solution(1)
    tier_2_solution(1)
    tier_3_solution(param=1)
    # tup_comp = (num for num in range(10))
    # list_comp = [num for num in range(10)]
