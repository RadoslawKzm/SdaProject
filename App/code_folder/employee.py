"""Employee class file"""
# builtin imports
from __future__ import annotations

# pip3 install imports
from typing import Dict, Union
from uuid import UUID, uuid4


class Employee:
    """input: name, last_name, age
    should create: email@company.com, uuid"""

    registry: Dict[UUID, Employee] = {}

    def __init__(self, *, name: str, last_name: str, age: int) -> None:
        if age < 1:
            raise ValueError("Age less than 0")
        if not all((name, last_name)):
            raise ValueError("name or last name missing")
        self.name: str = name
        self.last: str = last_name
        self.age: int = age
        self.email: str = self.create_email()
        self.company_id = self.create_uuid()
        self.update_registry(self=self)

    @classmethod
    def update_registry(cls, *, self: Employee) -> None:
        cls.registry[self.company_id] = self

    def create_email(self) -> str:
        return f"{self.name}.{self.last}@company.com"

    @staticmethod
    def create_uuid() -> UUID:
        return uuid4()

    @classmethod
    def get_json_registry(cls) -> list[Dict[str, Union[str, int]]]:
        """Return list of serialized and human readable employee objects:
        [{"name":"Jaroslaw", "last":"Dupa", "age":69, "email":"Jaroslaw.Dupa@company.com"},
        {"name":"Mirosław", "last":"Dupa2", "age":69, "email":"Mirosław.Dupa2@company.com"},
        {"name":"Janusz", "last":"Dupa3", "age":69, "email":"Janusz.Dupa3@company.com"},
        {"name":"Alojzy", "last":"Dupa4", "age":69, "email":"Alojzy.Dupa4@company.com"},
        {"name":"Waldemar", "last":"Dupa5", "age":69, "email":"Waldemar.Dupa5@company.com"}]"""
        output: list[Dict[str, Union[str, int]]] = []
        for emp_uuid, emp_obj in cls.registry.items():
            output.append(
                {
                    "name": emp_obj.name,
                    "last": emp_obj.last,
                    "age": emp_obj.age,
                    "email": emp_obj.email,
                }
            )
        return output
