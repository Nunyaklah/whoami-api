from uuid import uuid4
from fastapi import FastAPI
from model import Answer, Question
from typing import Optional, List

app = FastAPI()

db: List[Question] = [
    Question(
        id=uuid4(),
        question="You’re really busy at work and a colleague is telling you their life story and personal woes. You:",
        answers=[Answer(
            answer="Dont dare to interrupt them",
            point=0.5
        ),
            Answer(
            answer="Think its more important to give them some of your time; work can wait",
            point=0.5
        ),
            Answer(
            answer="Listen, but with only with half an ear",
            point=0.5
        ),
            Answer(
            answer="Interrupt and explain that you are really busy at the moment",
            point=0.5
        )
        ]
    ),
    Question(
        id=uuid4(),
        question="Youve been sitting in the doctors waiting room for more than 25 minutes. You:",
        answers=[Answer(
            answer="Look at your watch every two minutes",
            point=0.5
        ),
            Answer(
            answer="Bubble with inner anger, but keep quiet",
            point=0.5
        ),
            Answer(
            answer="Explain to other equally impatient people in the room that the doctor is always running late",
            point=0.5
        ),
            Answer(
            answer="Complain in a loud voice, while tapping your foot impatiently",
            point=0.5
        )
        ]
    ),
    Question(
        id=uuid4(),
        question="Youre having an animated discussion with a colleague regarding a project that youre in charge of. You:",
        answers=[Answer(
            answer="Dont dare contradict them",
            point=0.5
        ),
            Answer(
            answer="Think that they are obviously right",
            point=0.5
        ),
            Answer(
            answer="Defend your own point of view, tooth and nail",
            point=0.5
        ),
            Answer(
            answer="Continuously interrupt your colleague",
            point=0.5
        )
        ]
    ),
    Question(
        id=uuid4(),
        question="You are taking part in a guided tour of a museum. You:",
        answers=[Answer(
            answer="Are a bit too far towards the back so dont really hear what the guide is saying",
            point=0.5
        ),
            Answer(
            answer="Follow the group without question",
            point=0.5
        ),
            Answer(
            answer="Make sure that everyone is able to hear properly",
            point=0.5
        ),
            Answer(
            answer="Are right up the front, adding your own comments in a loud voice",
            point=0.5
        )
        ]
    ),
    Question(
        id=uuid4(),
        question="During dinner parties at your home, you have a hard time with people who:",
        answers=[Answer(
            answer="Ask you to tell a story in front of everyone else",
            point=0.5
        ),
            Answer(
            answer="Talk privately between themselves",
            point=0.5
        ),
            Answer(
            answer="Hang around you all evening",
            point=0.5
        ),
            Answer(
            answer="Always drag the conversation back to themselves",
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
    return db
