from dataclasses import dataclass

@dataclass
class Person:
    user_name: str = None
    user_surname: str = None
    phone_number: str = None
    email: str = None
    password: str = None

