from __future__ import annotations

"""Employee class file"""
from uuid import uuid4, UUID
from typing import Dict


class Employee:
    """input: name, last_name, age
    should create: email@company.com, uuid"""

    registry: Dict = {}

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

    def create_uuid(self) -> UUID:
        return uuid4()
