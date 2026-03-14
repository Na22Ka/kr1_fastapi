from fastapi import FastAPI
from fastapi.responses import FileResponse

from models import User, UserAge, Feedback, FeedbackStrict

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}


@app.get("/html")
def get_html():
    return FileResponse("index.html")


@app.post("/calculate")
def calculate(num1: float, num2: float):
    return {"result": num1 + num2}


current_user = User(name="Ваше Имя Фамилия", id=1)


@app.get("/users")
def get_user():
    return current_user


@app.post("/user")
def check_adult(user: UserAge):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult,
    }


feedbacks_basic = []


@app.post("/feedback")
def post_feedback(feedback: Feedback):
    feedbacks_basic.append({"name": feedback.name, "message": feedback.message})
    return {"message": f"Feedback received. Thank you, {feedback.name}."}



feedbacks_strict = []


@app.post("/feedback/strict")
def post_feedback_strict(feedback: FeedbackStrict):
    feedbacks_strict.append({"name": feedback.name, "message": feedback.message})
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}
