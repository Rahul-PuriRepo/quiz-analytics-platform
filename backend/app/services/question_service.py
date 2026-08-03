from app.repositories.question_repository import QuestionRepository


class QuestionService:
    def __init__(self):
        self.repository = QuestionRepository()

    def get_all_questions(self):
        questions = self.repository.get_all_questions()

        for question in questions:
            question.pop("correctOption", None)

        return questions