"""Employee class file"""
# builtin imports
from __future__ import annotations
from uuid import uuid4, UUID
from typing import Dict


class Employee:
    """input: name, last_name, age
    should create: email@company.com, uuid"""

    registry: Dict[UUID, Employee] = {}

    def __init__(self, *, name: str, last_name: str, age: int) -> None:
        if age < 1:
            raise ValueError("Age less than 0")
        if not all((name, last_name)):
            raise ValueError("name or last name missing")
        self.name = name
        self.last = last_name
        self.age = age
        self.email = self.create_email()
        self.company_id = self.create_uuid()
        self.update_registry(self=self)

    @classmethod
    def update_registry(cls, *, self: Employee):
        cls.registry[self.company_id] = self

    def create_email(self) -> str:
        return f"{self.name}.{self.last}@company.com"

    @staticmethod
    def create_uuid() -> UUID:
        return uuid4()

    @classmethod
    def get_json_registry(cls) -> list[dict]:
        """Return list of serialized and human readable employee objects:
        [{"name":"Jaroslaw", "last":"Dupa", "age":69, "email":"Jaroslaw.Dupa@company.com"},
        {"name":"Mirosław", "last":"Dupa2", "age":69, "email":"Mirosław.Dupa2@company.com"},
        {"name":"Janusz", "last":"Dupa3", "age":69, "email":"Janusz.Dupa3@company.com"},
        {"name":"Alojzy", "last":"Dupa4", "age":69, "email":"Alojzy.Dupa4@company.com"},
        {"name":"Waldemar", "last":"Dupa5", "age":69, "email":"Waldemar.Dupa5@company.com"}]"""
        pass

    """
    Resolved homework much more below
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    # @classmethod
    # def get_json_registry(cls) -> list:
    #     output: list = []
    #     for emp_uuid, emp_obj in cls.registry.items():
    #         output.append({"name": emp_obj.name, "last": emp_obj.last, "age": emp_obj.age, "email": emp_obj.email})
    #     return output
