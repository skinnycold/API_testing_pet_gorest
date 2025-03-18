from api.api_client import APIClient
from models.users_models import UserGenerate, UserPostGenerate, UserToDoGenerate


class UsersAPI(APIClient):
    def __init__(self):
        super().__init__()
        self.endpoint = '/users'

    def get_users(self, endpoint: str = None):
        endpoint = endpoint or self.endpoint
        self.response = self.get(endpoint)
        self.response_json = self.response.json()
        return self.response

    def get_user_details(self, endpoint: str = None, user_id: int = 7774502):
        endpoint = endpoint or self.endpoint
        self.response = self.get(f"{endpoint}/{user_id}")
        self.response_json = self.response.json()
        return self.response

    def create_new_user(self, data: dict, endpoint: str = None):
        endpoint = endpoint or self.endpoint
        self.response = self.post(endpoint, data)
        self.response_json = self.response.json()
        return self.response

    def update_user(self, data: dict, endpoint: str = None, user_id: int = None):
        endpoint = endpoint or self.endpoint
        self.response = self.put(f"{endpoint}/{user_id}", data)
        self.response_json = self.response.json()
        return self.response

    def delete_user(self, endpoint: str = None, user_id: int = None):
        endpoint = endpoint or self.endpoint
        self.response = self.delete(f"{endpoint}/{user_id}")
        return self.response

    def create_post_for_user(self, data: dict, user_id: int, endpoint: str = None):
        endpoint = endpoint or self.endpoint
        self.response = self.post(f"{endpoint}/{user_id}/posts", data)
        self.response_json = self.response.json()
        return self.response

    def get_user_posts(self, user_id: int, endpoint: str = None):
        endpoint = endpoint or self.endpoint
        self.response = self.get(f"{endpoint}/{user_id}/posts")
        self.response_json = self.response.json()
        return self.response

    def create_todo_for_user(self, data: dict, user_id: int, endpoint: str = None):
        endpoint = endpoint or self.endpoint
        self.response = self.post(f"{endpoint}/{user_id}/todos", data)
        self.response_json = self.response.json()
        return self.response

    def get_user_todos(self, user_id: int, endpoint: str = None):
        endpoint = endpoint or self.endpoint
        self.response = self.get(f"{endpoint}/{user_id}/todos")
        self.response_json = self.response.json()
        return self.response
