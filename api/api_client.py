import requests
from pydantic.v1 import ValidationError
from utils.config import API_TOKEN, API_URL
from utils.logger_config import get_logger
import allure

logger = get_logger(__name__)


class APIClient:
    def __init__(self):
        self.base_url = API_URL
        self.session = requests.session()
        self.session.headers.update({
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        })
        self.response = None
        self.response_json = None

    def _request(self, method, endpoint, data=None):
        """Универсальный метод для обработки запросов (GET, POST и др.)."""
        url = f"{self.base_url}{endpoint}"
        with allure.step(f"Осуществляем {method} - запрос к {url}, данные: {data}"):
            logger.info(f"Осуществляем {method} - запрос к {url}, данные: {data}")
            response = self.session.request(method, url, json=data)
            return response

    def get(self, endpoint):
        return self._request('GET', endpoint)

    def post(self, endpoint, data):
        return self._request('POST', endpoint, data)

    def put(self, endpoint, data):
        return self._request('PUT', endpoint, data)

    def delete(self, endpoint):
        return self._request('DELETE', endpoint)

    def check_status(self, expected_status_code: int = 200):
        """
        Проверяет статус код ответа от сервера с ожидаемым
        :param expected_status_code: Ожидаемый статус код
        """
        logger.info(
            f"""Проверяем статус ответа - Ожидаемый статус: {expected_status_code},
             Фактический статус: {self.response.status_code}"""
        )
        with allure.step(
                f"Проверяем статус код: Фактический {self.response.status_code}, Ожидаемый: {expected_status_code}"
        ):
            assert self.response.status_code == expected_status_code, f"""
            Ожидаемый статус код: {expected_status_code}
            Фактический статус код: {self.response.status_code}
            """
        logger.info("Статус соответствует ожидаемому")

    def check_json_schema(self, pydantic_schema):
        expected_scheme = pydantic_schema.model_json_schema()
        logger.info(
            f"Проверяем структуру JSON - Ожидаемая модель: {expected_scheme}, Фактический JSON: {self.response_json}"
        )
        with allure.step(f"Проверяем структуру JSON"):
            allure.attach(f"Ожидаемая модель: {expected_scheme}, Фактический JSON: {self.response_json}")
            try:
                pydantic_schema.model_validate(self.response_json)
                logger.info("JSON соответствует ожидаемой схеме")
            except ValidationError as e:
                logger.error("Ошибка валидации JSON-схемы!")
                logger.error(f"Детали ошибки:\n{e.json(indent=4)}")

    @allure.step("Сверяем данные из ответа с ожидаемыми")
    def validate_response(self, expected_data):
        """Метод для валидации JSON-ответа с ожидаемыми данными"""
        logger.info("Сверяем данные из ответа с ожидаемыми")
        for key, value in expected_data.items():
            assert self.response_json.get(key) == value, logger.error(f"Поле {key} не совпадает")
        logger.info("Данные совпадают")

    def close(self):
        """
        Закрываем соединение после работы
        """
        logger.info(
            f"""
            Закрываем сессию\n
            ---------------------------------------------------
            """
        )
        self.session.close()
