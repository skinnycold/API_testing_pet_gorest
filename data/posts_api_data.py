from utils.faker_generator import FakerGenerator

fg = FakerGenerator()
invalid_post_data = [
    ("", fg.random_text(20), fg.random_text(20), 422),
    ("7774659", "", fg.random_text(20), 422),
    ("7774659", fg.random_text(20), "", 422),
    ("215215215252525", fg.random_text(20), fg.random_text(20), 422),

]
