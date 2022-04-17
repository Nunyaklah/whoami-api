from uuid import uuid4
from fastapi import FastAPI
from model import Answer,  Question
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db: List[Question] = [
    Question(
        id=uuid4(),
        question="You’re really busy at work and a colleague is telling you their life story and personal woes. You:",
        answers=[Answer(
            option="A",
            answer="Dont dare to interrupt them",
            point=2
        ),
            Answer(
            option="B",
            answer="Think its more important to give them some of your time; work can wait",
            point=2
        ),
            Answer(
            option="C",
            answer="Listen, but with only with half an ear",
            point=1
        ),
            Answer(
            option="D",
            answer="Interrupt and explain that you are really busy at the moment",
            point=0.5
        )
        ]
    ),
    Question(
        id=uuid4(),
        question="Youve been sitting in the doctors waiting room for more than 25 minutes. You:",
        answers=[Answer(
            option="A",
            answer="Look at your watch every two minutes",
            point=1
        ),
            Answer(
            option="B",
            answer="Bubble with inner anger, but keep quiet",
            point=1
        ),
            Answer(
            option="C",
            answer="Explain to other equally impatient people in the room that the doctor is always running late",
            point=2
        ),
            Answer(
            option="D",
            answer="Complain in a loud voice, while tapping your foot impatiently",
            point=1
        )
        ]
    ),
    Question(
        id=uuid4(),
        question="Youre having an animated discussion with a colleague regarding a project that youre in charge of. You:",
        answers=[Answer(
            option="A",
            answer="Dont dare contradict them",
            point=0.5
        ),
            Answer(
            option="B",
            answer="Think that they are obviously right",
            point=1
        ),
            Answer(
            option="C",
            answer="Defend your own point of view, tooth and nail",
            point=0.5
        ),
            Answer(
            option="D",
            answer="Continuously interrupt your colleague",
            point=2
        )
        ]
    ),
    Question(
        id=uuid4(),
        question="You are taking part in a guided tour of a museum. You:",
        answers=[Answer(
            option="A",
            answer="Are a bit too far towards the back so dont really hear what the guide is saying",
            point=0.5
        ),
            Answer(
            option="B",
            answer="Follow the group without question",
            point=1
        ),
            Answer(
            option="C",
            answer="Make sure that everyone is able to hear properly",
            point=0.5
        ),
            Answer(
            option="D",
            answer="Are right up the front, adding your own comments in a loud voice",
            point=2
        )
        ]
    ),
    Question(
        id=uuid4(),
        question="During dinner parties at your home, you have a hard time with people who:",
        answers=[Answer(
            option="A",
            answer="Ask you to tell a story in front of everyone else",
            point=0.5
        ),
            Answer(
            option="B",
            answer="Talk privately between themselves",
            point=1
        ),
            Answer(
            option="C",
            answer="Hang around you all evening",
            point=2
        ),
            Answer(
            option="D",
            answer="Always drag the conversation back to themselves",
            point=5
        )
        ]
    )
]



@app.get("/")
def root():
    return {"Hello": "Welcome to Personality test"}


@app.get("/api/v1/questions")
async def fetch_questions():
    return db


@app.post("/api/v1/submit")
async def personality(point: int):
    point = point
    if point > 5:
        return "You are an Extrovert!!"
    else:
        return "You are an Introvert!!"

