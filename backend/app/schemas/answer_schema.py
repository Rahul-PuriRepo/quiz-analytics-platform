from pydantic import BaseModel


class AnswerRequest(BaseModel):
    questionId: int
    selectedOption: str
    timeTaken: int