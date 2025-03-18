invalid_user_data = [
        # Пустое имя
        ("", "male", "test@example.com", "active", 422),
        # Пустой пол
        ("John Doe", "", "test@example.com", "active", 422),
        # Пустой email
        ("John Doe", "male", "", "active", 422),
        # Пустой статус
        ("John Doe", "male", "test@example.com", "", 422),
        # Некорректный email
        ("John Doe", "male", "invalid_email", "active", 422),
        # Неизвестный статус
        ("John Doe", "male", "test@example.com", "unknown", 422),
        # Неизвестный пол
        ("John Doe", "unknown", "test@example.com", "active", 422),
        # Все поля пустые
        ("", "", "", "", 422)
    ]