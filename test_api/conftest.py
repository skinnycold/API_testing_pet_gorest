import pytest
from api.users_api import UsersAPI
from api.posts_api import PostsAPI
from models.users_models import UserValidate, UserGenerate
from models.posts_models import PostGenerate


@pytest.fixture()
def user_api():
    return UsersAPI()

@pytest.fixture()
def posts_api():
    return PostsAPI()

@pytest.fixture()
def create_user(user_api):
    user_data = UserGenerate().generate().model_dump()
    user_api.create_new_user(user_data)
    user_api.check_status(201)
    user_api.check_json_schema(UserValidate)
    user_id = user_api.response_json['id']
    yield user_id
    user_api.delete_user(user_id=user_id)
    user_api.close()

@pytest.fixture()
def create_post_fixture(create_user, posts_api):
    user_id = create_user
    user_data = PostGenerate.generate(user_id=user_id).model_dump()
    posts_api.create_post(data=user_data)
    post_id = posts_api.response_json['id']
    result = {
        "post_id":post_id,
        "user_id": user_id
    }
    return result