from api.api_client import APIClient

class PostsAPI(APIClient):
    def __init__(self):
        super().__init__()
        self.endpoint = '/posts'

    def get_posts(self, endpoint: str = None):
        endpoint = endpoint or self.endpoint
        self.response = self.get(endpoint)
        self.response_json = self.response.json()
        return self.response

    def get_specific_post(self, post_id, endpoint: str = None):
        endpoint = endpoint or self.endpoint
        self.response = self.get(f"{endpoint}/{post_id}")
        self.response_json = self.response.json()
        return self.response

    def create_post(self, data: dict, endpoint: str = None):
        endpoint = endpoint or self.endpoint
        self.response = self.post(endpoint, data=data)
        self.response_json = self.response.json()
        return self.response

    def update_post(self, post_id, data: dict, endpoint: str = None):
        endpoint = endpoint or self.endpoint
        self.response = self.put(f"{endpoint}/{post_id}", data=data)
        self.response_json = self.response.json()
        return self.response