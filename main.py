from uuid import uuid4
from fastapi import FastAPI
from model import Answer, Question
from typing import Optional, List

app = FastAPI()

db: List[Question] = [
    Question(
        id=uuid4(),
        question = "Youve been sitting in the doctor’s waiting room for more than 25 minutes. You:",
        answers=[Answer(
            answer="Complain in a loud voice, while tapping your foot impatiently",
            point=0.5
        ),
            Answer(
            answer="Complain in a loud voice, while tapping your foot impatiently",
            point=0.5
        )
        ]
    )
]


@app.get("/")
def root():
    return {"Hello": "Welcome to Personality test"}

@app.get("/api/v1/questions")
async def fetch_users():
    return db;    