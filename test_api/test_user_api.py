import pytest
import random
import allure
from models.users_models import (UserValidate, AllUsersValidate, UserPostValidate, AllPostsValidate,
                                 UserToDoValidate, AllToDoValidate, UserGenerate, UserPostGenerate,
                                 UserToDoGenerate)
from data.user_api_data import invalid_user_data



class TestUserAPIPositive:

    @allure.title("Получение всех пользователей")
    def test_get_users(self, user_api):
        user_api.get_users()
        user_api.check_status(200)
        user_api.check_json_schema(AllUsersValidate)

    @allure.title("Получение определенного пользователя")
    def test_get_user_details(self, user_api):
        user_api.get_user_details()
        user_api.check_status(200)
        user_api.check_json_schema(UserValidate)

    @allure.title("Создание пользователя")
    def test_create_user(self, user_api):
        user_data = UserGenerate().generate().model_dump()
        user_api.create_new_user(user_data)
        user_api.check_status(201)
        user_api.check_json_schema(UserValidate)
        user_api.validate_response(user_data)
        user_id = user_api.response_json['id']
        user_api.get_user_details(user_id=user_id)
        user_api.check_status()
        user_api.validate_response(user_data)
        user_api.delete_user(user_id=user_id)

    @allure.title("Редактирование пользователя")
    def test_update_user(self, user_api, create_user):
        user_data = UserGenerate().generate().model_dump()
        user_api.update_user(user_data, user_id=create_user)
        user_api.check_status(200)
        user_api.validate_response(user_data)
        user_api.check_json_schema(UserValidate)

    @allure.title("Удаление пользователя")
    def test_delete_user(self, user_api, create_user):
        user_api.delete_user(user_id=create_user)
        user_api.check_status(204)
        user_api.get_user_details(user_id=create_user)
        user_api.check_status(404)

    @allure.title("Создание поста для пользователя")
    def test_create_user_post(self, user_api, create_user):
        post_data = UserPostGenerate.generate().model_dump()
        user_api.create_post_for_user(post_data, create_user)
        user_api.check_status(201)
        user_api.validate_response(post_data)
        user_api.check_json_schema(UserPostValidate)

    @allure.title("Получение пользовательских постов")
    def test_get_user_post(self, user_api, create_user):
        post_data = UserPostGenerate.generate().model_dump()
        user_api.create_post_for_user(data=post_data, user_id=create_user)
        user_api.check_status(201)
        user_api.check_json_schema(UserPostValidate)
        user_api.get_user_posts(create_user)
        user_api.check_status(200)
        user_api.check_json_schema(AllPostsValidate)

    @allure.title("Создание плана")
    def test_create_user_todo(self, user_api, create_user):
        todo_body = UserToDoGenerate.generate().model_dump()
        user_api.create_todo_for_user(data=todo_body, user_id=create_user)
        user_api.check_status(201)
        user_api.validate_response(todo_body)
        user_api.check_json_schema(UserToDoValidate)

    @allure.title("Получение пользовательских планов")
    def test_get_user_todo(self, user_api, create_user):
        todo_body = UserToDoGenerate.generate().model_dump()
        user_api.create_todo_for_user(data=todo_body, user_id=create_user)
        user_api.check_status(201)
        user_api.check_json_schema(UserToDoValidate)
        user_api.get_user_todos(create_user)
        user_api.check_status(200)
        user_api.check_json_schema(AllToDoValidate)



class TestUserAPINegative:

    @allure.title("Получение пользователя")
    def test_get_user_details_negative(self, user_api):
        user_api.get_user_details(user_id=random.randint(11111111, 132612612612))
        user_api.check_status(404)

    @pytest.mark.parametrize(
        "name, gender, email, status, expected_status",
        invalid_user_data
    )
    @allure.title("Создание пользователя")
    def test_create_user_negative(self, user_api, name, gender, email, status, expected_status):
        data = {
            "name": name,
            "gender": gender,
            "email": email,
            "status": status
        }
        user_api.create_new_user(data=data)
        user_api.check_status(expected_status)

    @pytest.mark.parametrize(
        "name, gender, email, status, expected_status",
        invalid_user_data
    )
    @allure.title("Редактирование пользователя")
    def test_update_user_negative(self, user_api, create_user, name, gender, email, status, expected_status):
        data = {
            "name": name,
            "gender": gender,
            "email": email,
            "status": status
        }
        user_api.update_user(data=data, user_id=create_user)
        user_api.check_status(expected_status)

    @pytest.mark.parametrize(
        "title, body, expected_status",
        [("", "this is body", 422), ("this is title", "", 422)]
    )
    @allure.title("Создание пользовательского поста")
    def test_create_user_post_negative(self, user_api, create_user, title, body, expected_status):
        data = {
            "title": title,
            "body": body
        }
        user_api.create_post_for_user(user_id=create_user, data=data)
        user_api.check_status(expected_status)

    @pytest.mark.parametrize(
        "title, status, expected_status",
        [("", "pending", 422), ("this is title", "", 422), ("this is title", "unknown", 422)]
    )
    @allure.title("Создание пользовательского плана")
    def test_create_user_todo(self, user_api, create_user, title, status, expected_status):
        data = {
            "title": title,
            "status": status
        }
        user_api.create_todo_for_user(user_id=create_user, data=data)
        user_api.check_status(expected_status)
