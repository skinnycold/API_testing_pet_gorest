
# API Testing Pet Project

Этот проект представляет собой **автоматизированные тесты для API**, которые используют библиотеки **pytest**, **Allure** для отчетности и **GitHub Actions** для CI/CD.

## Описание

В этом проекте реализовано тестирование API с использованием библиотеки **pytest**. В процессе тестирования генерируются **Allure отчеты**, которые автоматически выгружаются на **GitHub Pages** после прохождения тестов.

## Технологии

- **Python 3.11**
- **pytest** - для написания тестов
- **Allure** - для генерации отчетов
- **GitHub Actions** - для CI/CD
- **requests** - для HTTP-запросов

## Установка

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/skinnycold/API_testing_pet_gorest.git
   cd API_testing_pet_gorest
   ```

2. Создай и активируй виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   .\venv\Scripts\activate  # Для Windows
   ```

3. Установи зависимости:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Запуск тестов локально

Чтобы запустить тесты локально, выполните команду:
```bash
pytest --alluredir=allure-results
```

После выполнения тестов, чтобы сгенерировать Allure-отчет, используйте:
```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## GitHub Actions

### Запуск тестов вручную
Чтобы вручную запустить тесты и опубликовать отчет:
1. Перейди в раздел **Actions** репозитория.
2. Нажми **Run workflow**.
3. Выбери **Run workflow** и выбери параметр для запуска.

## Развертывание отчетов

После завершения тестов, Allure-отчет автоматически публикуется на **GitHub Pages** и доступен по следующему пути:
```
https://skinnycold.github.io/API_testing_pet_gorest/
```
