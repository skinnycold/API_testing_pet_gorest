from faker import Faker

class FakerGenerator:
    def __init__(self):
        self.faker = Faker()

    def full_name(self):
        return self.faker.name()

    def email(self):
        return self.faker.email()

    def random_text(self, qty_char: int = 20):
        return self.faker.text(qty_char)