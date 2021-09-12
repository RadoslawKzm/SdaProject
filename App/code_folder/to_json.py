from employee import Employee


def to_json_resolved(self: Employee) -> dict:
    return {self.company_id: {"name": self.name, "last": self.last, "age": self.age, "email": self.email}}
