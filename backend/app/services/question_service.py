from app.repositories.question_repository import (
    QuestionRepository,
)


class QuestionService:

    def __init__(self):
        self.repository = QuestionRepository()

    def get_questions(self):
        return self.repository.get_all_questions()

    def get_question(self, question_id):
        return self.repository.get_question_by_id(
            question_id
        )