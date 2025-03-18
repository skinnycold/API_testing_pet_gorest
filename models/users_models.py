from pydantic import BaseModel, RootModel, Field
from utils.faker_generator import FakerGenerator
from typing import Literal
import random
fg = FakerGenerator()

class UserGenerate(BaseModel):
    name: str = Field(default_factory=lambda: fg.full_name())
    gender: Literal['male', 'female'] = Field(default_factory=lambda: random.choice(['male', 'female']))
    email: str = Field(default_factory=lambda: fg.email())
    status: Literal['active', 'inactive'] = Field(default_factory=lambda: random.choice(['active', 'inactive']))

    @classmethod
    def generate(cls, **kwargs) -> "UserGenerate":
        """Создаёт новый payload с возможностью переопределить значения."""
        return cls(**kwargs)

class UserValidate(BaseModel):
    id: int
    name: str
    email: str = Field(default_factory=lambda: fg.email(), pattern=r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{1,}$')
    gender: Literal['male', 'female']
    status: Literal['active', 'inactive']

class AllUsersValidate(RootModel[list[UserValidate]]):
    pass


class UserPostGenerate(BaseModel):
    title: str = Field(default_factory=lambda: fg.random_text(random.randint(5,50)))
    body: str = Field(default_factory=lambda: fg.random_text(random.randint(20,150)))

    @classmethod
    def generate(cls, **kwargs) -> "UserPostGenerate":
        """Создаёт новый payload с возможностью переопределить значения."""
        return cls(**kwargs)

class UserPostValidate(BaseModel):
    id: int
    user_id: int
    title: str
    body: str

class AllPostsValidate(RootModel[list[UserPostValidate]]):
    pass

class UserToDoGenerate(BaseModel):
    title: str = Field(default_factory=lambda: fg.random_text(random.randint(5, 50)))
    status: Literal["pending", "completed"] = Field(default_factory=lambda: random.choice(["pending", "completed"]))

    @classmethod
    def generate(cls, **kwargs) -> "UserToDoGenerate":
        return cls(**kwargs)

class UserToDoValidate(BaseModel):
    id: int
    user_id: int
    title: str
    due_on: str | None
    status: Literal["pending", "completed"]

class AllToDoValidate(RootModel[list[UserToDoValidate]]):
    pass
