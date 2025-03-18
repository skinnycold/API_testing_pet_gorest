import pytest
import allure
from models.posts_models import AllPostsValidate, PostGenerate, PostValidate
import random
from data.posts_api_data import invalid_post_data



class TestPostsAPIPositive:
    @allure.title("Получение всех постов")
    def test_get_posts(self, posts_api):
        posts_api.get_posts()
        posts_api.check_status(200)
        posts_api.check_json_schema(AllPostsValidate)

    @allure.title("Получение определенного поста")
    def test_get_specific_post(self, posts_api, create_post_fixture):
        posts_api.get_specific_post(post_id=create_post_fixture['post_id'])
        posts_api.check_status(200)
        posts_api.check_json_schema(PostValidate)

    @allure.title("Создание поста")
    def test_create_post(self, posts_api, create_user):
        user_data = PostGenerate.generate(user_id=create_user).model_dump()
        posts_api.create_post(data=user_data)
        posts_api.check_status(201)
        posts_api.check_json_schema(PostValidate)
        posts_api.validate_response(user_data)
        post_id = posts_api.response_json['id']
        posts_api.get_specific_post(post_id=post_id)
        posts_api.validate_response(user_data)
        posts_api.check_status(200)

    @allure.title("Редактирование поста")
    def test_update_post(self, posts_api, create_post_fixture):
        user_data = PostGenerate.generate(user_id=create_post_fixture['user_id']).model_dump()
        posts_api.update_post(post_id=create_post_fixture['post_id'], data=user_data)
        posts_api.check_status(200)
        posts_api.validate_response(user_data)



class TestPostsAPINegative:
    @allure.title("Получение поста")
    def test_get_specific_post_negative(self, posts_api):
        posts_api.get_specific_post(post_id=random.randint(11111111, 999999999))
        posts_api.check_status(404)

    @pytest.mark.parametrize(
        "user_id, title, body, expected_code",
        invalid_post_data
    )
    @allure.title("Создание поста")
    def test_create_post_negative(self, posts_api, create_user, user_id, title, body, expected_code):
        user_data = {
            "user_id": user_id,
            "title": title,
            "body": body
        }
        posts_api.create_post(data=user_data)
        posts_api.check_status(expected_code)

    @pytest.mark.parametrize(
        "user_id, title, body, expected_code",
        invalid_post_data
    )
    @allure.title("Редактирование поста")
    def test_update_post_negative(self, posts_api, create_post_fixture, create_user, user_id, title, body,
                                  expected_code):
        user_data = {
            "user_id": user_id,
            "title": title,
            "body": body
        }
        posts_api.update_post(post_id=create_post_fixture['post_id'], data=user_data)
        posts_api.check_status(expected_code)
