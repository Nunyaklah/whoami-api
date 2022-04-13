from pydantic import BaseModel
from uuid import uuid4
from uuid import UUID
from typing import Optional, List


class Answer(BaseModel):
    answer: str
    point: float


class Question(BaseModel):
    id: Optional[UUID] = uuid4()
    question: str
    answers: List[Answer]
