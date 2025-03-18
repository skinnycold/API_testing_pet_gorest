from pydantic import BaseModel, RootModel, Field
from utils.faker_generator import FakerGenerator
fg = FakerGenerator()
class PostValidate(BaseModel):
    id: int
    user_id: int
    title: str
    body: str

class AllPostsValidate(RootModel[list[PostValidate]]):
    pass

class PostGenerate(BaseModel):
    user_id: int | None
    title: str = Field(default_factory=lambda: fg.random_text(30))
    body: str = Field(default_factory=lambda: fg.random_text(100))

    @classmethod
    def generate(cls, **kwargs) -> "PostGenerate":
        return cls(**kwargs)

