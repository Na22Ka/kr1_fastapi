from pydantic import BaseModel, Field, field_validator
import re


# Задание 1.4 — модель пользователя с id
class User(BaseModel):
    name: str
    id: int


# Задание 1.5 — модель пользователя с возрастом
class UserAge(BaseModel):
    name: str
    age: int


# Задание 2.1 — модель отзыва (базовая)
class Feedback(BaseModel):
    name: str
    message: str


# Задание 2.2 — модель отзыва с валидацией
BANNED_WORDS = ["кринж", "рофл", "вайб"]


class FeedbackStrict(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator("message")
    @classmethod
    def check_banned_words(cls, value: str) -> str:
        for word in BANNED_WORDS:
            # Ищем слово по первым 4 символам, чтобы поймать любые падежи
            if re.search(word[:4], value, re.IGNORECASE):
                raise ValueError("Использование недопустимых слов")
        return value
