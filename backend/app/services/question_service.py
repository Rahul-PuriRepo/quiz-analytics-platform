from app.repositories.question_repository import QuestionRepository
from fastapi import HTTPException


class QuestionService:
    def __init__(self):
        self.repository = QuestionRepository()

    def get_all_questions(self):
        questions = self.repository.get_all_questions()

        for question in questions:
            question.pop("correctOption", None)

        return questions

    def get_question_by_id(self, question_id: int):
        question = self.repository.get_question_by_id(question_id)
        if question is None:
            raise HTTPException(
                status_code=404,
                detail="Question not found",
            )

        question.pop("correctOption", None)

        return question